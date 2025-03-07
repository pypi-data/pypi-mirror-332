import time
import logging
import heapq
from pathlib import Path

import jieba

from .candidate import Candidate
from .keystroke_map_db import KeystrokeMappingDB
from .core.custom_decorators import lru_cache_with_doc, deprecated
from .core.F import (
    modified_levenshtein_distance,
    is_chinese_character,
    is_all_chinese_char,
)
from .ime import (
    IMEFactory,
    BOPOMOFO_IME,
    CANGJIE_IME,
    ENGLISH_IME,
    PINYIN_IME,
    SPECIAL_IME,
)
from .phrase_db import PhraseDataBase
from .muti_config import MultiConfig


from .ime import (
    BOPOMOFO_VALID_KEYSTROKE_SET,
    ENGLISH_VALID_KEYSTROKE_SET,
    PINYIN_VALID_KEYSTROKE_SET,
    CANGJIE_VALID_KEYSTROKE_SET,
)

TOTAL_VALID_KEYSTROKE_SET = (
    BOPOMOFO_VALID_KEYSTROKE_SET.union(ENGLISH_VALID_KEYSTROKE_SET)
    .union(PINYIN_VALID_KEYSTROKE_SET)
    .union(CANGJIE_VALID_KEYSTROKE_SET)
)

CHINESE_PHRASE_DB_PATH = Path(__file__).parent / "src" / "chinese_phrase.db"
USER_PHRASE_DB_PATH = Path(__file__).parent / "src" / "user_phrase.db"
USER_FREQUENCY_DB_PATH = Path(__file__).parent / "src" / "user_frequency.db"

MAX_SAVE_PRE_POSSIBLE_SENTENCES = 5


class KeyEventHandler:
    def __init__(self, verbose_mode: bool = False) -> None:
        # Setup logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO if verbose_mode else logging.WARNING)
        self.logger.addHandler(logging.StreamHandler())

        # Setup Config
        self.muti_config = MultiConfig()
        self._chinese_phrase_db = PhraseDataBase(CHINESE_PHRASE_DB_PATH)
        self._user_phrase_db = PhraseDataBase(USER_PHRASE_DB_PATH)
        self._user_frequency_db = KeystrokeMappingDB(USER_FREQUENCY_DB_PATH)

        # Setup IMEs
        self.actived_imes: list[str] = self.muti_config.ACTIVE_IME
        self.ime_handlers = {
            ime: IMEFactory.create_ime(ime) for ime in self.actived_imes
        }

        # Config Settings
        self.AUTO_PHRASE_LEARN = self.muti_config.AUTO_PHRASE_LEARN
        self.AUTO_FREQUENCY_LEARN = self.muti_config.AUTO_FREQUENCY_LEARN
        self.SELECTION_PAGE_SIZE = self.muti_config.SELECTION_PAGE_SIZE

        # State Variables
        self._token_pool_set = set()
        self._pre_possible_sentences = []
        self.have_selected = False

        self.freezed_index = 0
        self.freezed_token_sentence = []
        self.freezed_composition_words = []

        self.unfreezed_keystrokes = ""
        self.unfreezed_token_sentence = []
        self.unfreezed_composition_words = []

        # Selection States
        self.in_selection_mode = False
        self._total_selection_index = 0
        self._total_candidate_word_list = []

    def _reset_all_states(self) -> None:
        self._token_pool_set = set()
        self._pre_possible_sentences = []
        self.have_selected = False

        self.freezed_index = 0
        self.freezed_token_sentence = []
        self.freezed_composition_words = []

        self.unfreezed_keystrokes = ""
        self.unfreezed_token_sentence = []
        self.unfreezed_composition_words = []

        self._reset_selection_states()

    def _reset_selection_states(self) -> None:
        self.in_selection_mode = False
        self._total_selection_index = 0
        self._total_candidate_word_list = []

    def _unfreeze_to_freeze(self) -> None:
        self._token_pool_set = set()
        self._pre_possible_sentences = []
        self.freezed_token_sentence = self.separate_english_token(
            self.total_token_sentence
        )  # Bad design here
        self.freezed_composition_words = self.separate_english_token(
            self.total_composition_words
        )
        self.freezed_index = self.freezed_index + len(
            self.separate_english_token(self.unfreezed_composition_words)
        )

        self.unfreezed_keystrokes = ""
        self.unfreezed_token_sentence = []
        self.unfreezed_composition_words = []

    def separate_english_token(self, tokens: list[str]) -> list[str]:
        #  Special case for English, separate the english word by character
        result = []
        for token in tokens:
            if self.ime_handlers[ENGLISH_IME].is_valid_token(token):
                result.extend([c for c in token])
            else:
                result.append(token)
        return result

    def set_activation_status(self, ime_type: str, status: bool) -> None:
        self.muti_config.setIMEActivationStatus(ime_name=ime_type, status=status)
        self.actived_imes = self.muti_config.ACTIVE_IME

    @property
    def token_pool(self) -> list[str]:
        return list(self._token_pool_set)

    @property
    def total_composition_words(self) -> list[str]:
        return (
            self.freezed_composition_words[: self.freezed_index]
            + self.unfreezed_composition_words
            + self.freezed_composition_words[self.freezed_index :]
        )

    @property
    def total_token_sentence(self) -> list[str]:
        return (
            self.freezed_token_sentence[: self.freezed_index]
            + self.unfreezed_token_sentence
            + self.freezed_token_sentence[self.freezed_index :]
        )

    @property
    def composition_index(self) -> int:
        return self.freezed_index + self.unfreezed_index

    @property
    def unfreezed_index(self) -> int:
        return len(self.unfreezed_composition_words)

    @property
    def candidate_word_list(self) -> list[str]:
        """
        The candidate word list for the current token in selection mode.
        Show only the current page of the candidate word list.
        """
        page = self._total_selection_index // self.SELECTION_PAGE_SIZE
        return self._total_candidate_word_list[
            page * self.SELECTION_PAGE_SIZE : (page + 1) * self.SELECTION_PAGE_SIZE
        ]

    @property
    def selection_index(self) -> int:
        return self._total_selection_index % self.SELECTION_PAGE_SIZE

    @property
    def composition_string(self) -> str:
        return "".join(self.total_composition_words)

    def handle_key(self, key: str) -> None:
        special_keys = ["enter", "left", "right", "down", "up", "esc"]
        if key in special_keys:
            if self.in_selection_mode:
                if key == "down":
                    if (
                        self._total_selection_index
                        < len(self._total_candidate_word_list) - 1
                    ):
                        self._total_selection_index += 1
                elif key == "up":
                    if self._total_selection_index > 0:
                        self._total_selection_index -= 1
                elif (
                    key == "enter"
                ):  # Overwrite the composition string & reset selection states
                    self.have_selected = True
                    selected_word = self._total_candidate_word_list[
                        self._total_selection_index
                    ]
                    self.freezed_composition_words[self.composition_index - 1] = (
                        selected_word
                    )
                    # ! Recaculate the index
                    self.freezed_index = self.freezed_index + len(selected_word) - 1
                    self._reset_selection_states()
                elif key == "left":  # Open side selection ?
                    pass
                elif key == "right":
                    pass
                elif key == "esc":
                    self._reset_selection_states()
                else:
                    print(f"Invalid Special key: {key}")

                return
            else:
                if (
                    key == "enter"
                ):  # Conmmit the composition string, update the db & reset all states
                    self._unfreeze_to_freeze()
                    if self.AUTO_PHRASE_LEARN:
                        self.update_user_phrase_db(self.composition_string)
                    if self.AUTO_FREQUENCY_LEARN:
                        self.update_user_frequency_db()
                    self._reset_all_states()
                elif key == "left":
                    self._unfreeze_to_freeze()
                    if self.freezed_index > 0:
                        self.freezed_index -= 1
                elif key == "right":
                    self._unfreeze_to_freeze()
                    if self.freezed_index < len(self.total_composition_words):
                        self.freezed_index += 1
                elif key == "down":  # Enter selection mode
                    self._unfreeze_to_freeze()
                    if (
                        len(self.total_token_sentence) > 0
                        and self.composition_index > 0
                    ):
                        token = self.total_token_sentence[self.composition_index - 1]
                        if not self.ime_handlers[ENGLISH_IME].is_valid_token(token):
                            self._total_candidate_word_list = (
                                self._get_token_candidate_words(token)
                            )
                            if len(self._total_candidate_word_list) > 1:
                                # Only none-english token can enter selection mode, and
                                # the candidate list should have more than 1 candidate
                                self.in_selection_mode = True
                elif key == "esc":
                    self._reset_all_states()
                else:
                    print(f"Invalid Special key: {key}")

                return
        else:
            if key == "backspace":
                if self.unfreezed_index > 0:
                    self.unfreezed_keystrokes = self.unfreezed_keystrokes[:-1]
                    self.unfreezed_composition_words = self.unfreezed_composition_words[
                        :-1
                    ] + [self.unfreezed_token_sentence[-1][:-1]]
                else:
                    if self.freezed_index > 0:
                        self.freezed_composition_words = (
                            self.freezed_composition_words[: self.freezed_index - 1]
                            + self.freezed_composition_words[self.freezed_index :]
                        )
                        self.freezed_index -= 1
                        return
            elif key == "space":
                self.unfreezed_keystrokes += " "
                self.unfreezed_composition_words += [" "]
            elif key in TOTAL_VALID_KEYSTROKE_SET:
                self.unfreezed_keystrokes += key
                self.unfreezed_composition_words += [key]
            elif key.startswith("©"):
                self.unfreezed_keystrokes += key
                self.unfreezed_composition_words += [key[1:]]
            else:
                print(f"Invalid key: {key}")
                return

    def slow_handle(self):
        # Migration to v2
        self._slow_handle_v2()
        return
    
        # Update the token pool
        start_time = time.time()
        self._update_token_pool()
        self.logger.info(f"Updated token pool: {time.time() - start_time}")
        self.logger.info(f"Token pool: {self.token_pool}")

        # Reconstruct the sentence
        start_time = time.time()
        possible_sentences = self._reconstruct_sentence_from_pre_possible_sentences(
            self.unfreezed_keystrokes
        )
        self.logger.info(f"Reconstructed sentence: {time.time() - start_time}")
        self.logger.info(f"Reconstructed sentences: {possible_sentences}")

        if possible_sentences == []:
            self.logger.info("No possible sentences found")
            return

        # Calculate the distance of the possible sentences
        start_time = time.time()
        possible_sentences = self._sort_possible_sentences(possible_sentences)
        best_sentences = possible_sentences[0]
        self._pre_possible_sentences = possible_sentences[
            :MAX_SAVE_PRE_POSSIBLE_SENTENCES
        ]
        self.unfreezed_token_sentence = best_sentences
        self.logger.info(f"Filtered sentence: {time.time() - start_time}")
        self.logger.info(f"Best sentences: {best_sentences}")
        self.logger.info(f"Pre possible sentences: {self._pre_possible_sentences}")

        start_time = time.time()
        self.unfreezed_composition_words = self._token_sentence_to_word_sentence(
            best_sentences
        )
        self.logger.info(f"Token to word sentence: {time.time() - start_time}")
        self.logger.info(f"Token to word sentences: {self.unfreezed_composition_words}")

        return

    def _update_token_pool(self) -> None:
        for ime_type in self.actived_imes:
            token_ways = self.ime_handlers[ime_type].tokenize(self.unfreezed_keystrokes)
            for ways in token_ways:
                for token in ways:
                    self._token_pool_set.add(token)

        # Cut large token to small token
        # TODO: This is a hack, need to find a better way to handle this
        sorted_tokens = sorted(
            list(self._token_pool_set), key=lambda x: len(x), reverse=True
        )
        for token in sorted_tokens:
            if len(token) > 1:
                for i in range(1, len(token)):
                    if token[:i] in self._token_pool_set:
                        self._token_pool_set.add(token[i:])

    def _is_token_in_pool(self, token: str) -> bool:
        return token in self._token_pool_set

    @lru_cache_with_doc(maxsize=128)
    def get_token_distance(self, request_token: str) -> int:
        return self._closest_word_distance(request_token)

    # @lru_cache_with_doc(maxsize=128)
    def token_to_candidates(self, token: str) -> list[Candidate]:
        """
        Get the possible candidates of the token from all IMEs.

        Args:
            token (str): The token to search for
        Returns:
            list: A list of **Candidate** containing the possible candidates
        """
        candidates = []

        for ime_type in self.actived_imes:
            if self.ime_handlers[ime_type].is_valid_token(token):
                result = self.ime_handlers[ime_type].get_token_candidates(token)
                candidates.extend(
                    [
                        Candidate(
                            word,
                            key,
                            frequency,
                            token,
                            modified_levenshtein_distance(key, token),
                            ime_type,
                        )
                        for key, word, frequency in result
                    ]
                )

        if len(candidates) == 0:
            self.logger.info(f"No candidates found for token '{token}'")
            return [Candidate(token, token, 0, token, 0, "NO_IME")]

        candidates = sorted(
            candidates, key=lambda x: x.distance
        )  # First sort by distance
        candidates = sorted(
            candidates, key=lambda x: x.word_frequency, reverse=True
        )  # Then sort by frequency

        # FIXME: This is a hack to increase the rank of the token if it is in the user frequency db
        new_candidates = []
        for candidate in candidates:
            if self._user_frequency_db.word_exists(candidate.word):
                new_candidates.append(
                    (
                        candidate,
                        self._user_frequency_db.get_word_frequency(candidate.word),
                    )
                )
            else:
                new_candidates.append((candidate, 0))
        new_candidates = sorted(new_candidates, key=lambda x: x[1], reverse=True)
        candidates = [candidate[0] for candidate in new_candidates]

        return candidates

    def _get_token_candidate_words(self, token: str) -> list[str]:
        """
        Get the possible candidate words of the token from all IMEs.

        Args:
            token (str): The token to search for
        Returns:
            list: A list of **str** containing the possible candidate words
        """

        candidates = self.token_to_candidates(token)
        return [candidate.word for candidate in candidates]

    def _sort_possible_sentences(
        self, possible_sentences: list[list[str]]
    ) -> list[list[str]]:
        # Sort the possible sentences by the distance
        possible_sentences_with_distance = [
            dict(
                sentence=sentence,
                distance=self._calculate_sentence_distance(sentence),
            )
            for sentence in possible_sentences
        ]
        possible_sentences_with_distance = sorted(
            possible_sentences_with_distance, key=lambda x: x["distance"]
        )
        min_distance = possible_sentences_with_distance[0]["distance"]
        possible_sentences_with_distance = [
            r for r in possible_sentences_with_distance if r["distance"] <= min_distance
        ]

        # Sort the possible sentences by the number of tokens
        possible_sentences = sorted(
            possible_sentences_with_distance, key=lambda x: len(x["sentence"])
        )
        return [r["sentence"] for r in possible_sentences]

    def _token_sentence_to_word_sentence(
        self, token_sentence: list[str], context: str = ""
    ) -> list[str]:

        def solve_sentence_phrase_matching(
            sentence_candidate: list[list[Candidate]], pre_word: str = ""
        ):
            # TODO: Consider the context
            def recursive(best_sentence_tokens: list[list[Candidate]]) -> list[str]:
                if not best_sentence_tokens:
                    return []

                related_phrases = []
                for candidate in best_sentence_tokens[0]:
                    related_phrases.extend(
                        self._chinese_phrase_db.get_phrase_with_prefix(candidate.word)
                    )
                    related_phrases.extend(
                        self._user_phrase_db.get_phrase_with_prefix(candidate.word)
                    )

                related_phrases = [phrase[0] for phrase in related_phrases]
                related_phrases = [
                    phrase
                    for phrase in related_phrases
                    if len(phrase) <= len(best_sentence_tokens)
                ]
                related_phrases = sorted(
                    related_phrases, key=lambda x: len(x), reverse=True
                )

                for phrase in related_phrases:
                    correct_phrase = True
                    for i, char in enumerate(phrase):
                        if char not in [
                            candidate.word for candidate in best_sentence_tokens[i]
                        ]:
                            correct_phrase = False
                            break

                    if correct_phrase:
                        return [c for c in phrase] + recursive(
                            best_sentence_tokens[len(phrase) :]
                        )

                return [best_sentence_tokens[0][0].word] + recursive(
                    best_sentence_tokens[1:]
                )

            return recursive(sentence_candidate)

        def solve_sentence_naive_first(
            sentence_candidate: list[list[Candidate]],
        ) -> list[str]:
            return [c[0].word for c in sentence_candidate]

        sentence_candidates = [
            self.token_to_candidates(token) for token in token_sentence
        ]

        pre_word = context[-1] if context else ""
        result = solve_sentence_phrase_matching(sentence_candidates, pre_word)
        # result = solve_sentence_naive_first(sentence_candidates)
        return result

    def _reconstruct_sentence_from_pre_possible_sentences(
        self, target_keystroke: str
    ) -> list[list[str]]:
        try:
            possible_sentences = []

            if self._pre_possible_sentences != []:
                current_best_sentence = "".join(self._pre_possible_sentences[0])

                if len(target_keystroke) >= len(current_best_sentence):
                    for pre_possible_sentence in self._pre_possible_sentences:
                        subtracted_string = target_keystroke[
                            len("".join(pre_possible_sentence[:-1])) :
                        ]  # Get the remaining string that haven't been processed
                        possible_sentences.extend(
                            [
                                pre_possible_sentence[:-1] + sub_sentence_results
                                for sub_sentence_results in self._reconstruct_sentence(
                                    subtracted_string
                                )
                            ]
                        )
                else:  # The target_keystroke is shorter than the current best sentence, (e.g. backspace)
                    for pre_possible_sentence in self._pre_possible_sentences:
                        if "".join(pre_possible_sentence[:-1]).startswith(
                            target_keystroke
                        ):
                            possible_sentences.append(pre_possible_sentence[:-1])

                assert (
                    possible_sentences != []
                ), "No possible sentences found in the case of pre_possible_sentences"
            else:
                possible_sentences = self._reconstruct_sentence(target_keystroke)
        except AssertionError as e:
            self.logger.info(e)
            possible_sentences = self._reconstruct_sentence(target_keystroke)

        return possible_sentences

    def _reconstruct_sentence(self, keystroke: str) -> list[list[str]]:
        """
        Reconstruct the sentence back to the keystroke by searching all the
        possible combination of tokens in the token pool.

        Args:
            keystroke (str): The keystroke to search for
        Returns:
            list: A list of **list of str** containing the possible sentences constructed from the token pool
        """

        def dp_search(keystroke: str, token_pool: set[str]) -> list[list[str]]:
            if not keystroke:
                return []

            ans = []
            for token_str in token_pool:
                if keystroke.startswith(token_str):
                    ans.extend(
                        [
                            [token_str] + sub_ans
                            for sub_ans in dp_search(
                                keystroke[len(token_str) :], token_pool
                            )
                            if sub_ans
                        ]
                    )

            if keystroke in token_pool:
                ans.append([keystroke])
            return ans

        token_pool = set(
            [
                token
                for token in self.token_pool
                if self.get_token_distance(token) != float("inf")
            ]
        )
        result = dp_search(keystroke, token_pool)
        if not result:
            token_pool = set([token for token in self.token_pool])
            result = dp_search(keystroke, token_pool)

        return result

    def _calculate_sentence_distance(self, sentence: list[str]) -> int:
        """
        Calculate the distance of the sentence based on the token pool.

        Args:
            sentence (list): The sentence to calculate the distance
        Returns:
            int: The distance of the sentence
        """

        return sum([self.get_token_distance(token) for token in sentence])

    @lru_cache_with_doc(maxsize=128)
    def _closest_word_distance(self, token: str) -> int:
        """
        Get the word distance to the closest word from all IMEs.

        Args:
            token (str): The token to search for
        Returns:
            int: The distance to the closest word
        """
        min_distance = float("inf")

        if not self._is_token_in_pool(token):
            return min_distance

        for ime_type in self.actived_imes:
            if not self.ime_handlers[ime_type].is_valid_token(token):
                continue

            method_distance = self.ime_handlers[ime_type].closest_word_distance(token)
            min_distance = min(min_distance, method_distance)
        return min_distance

    def update_user_frequency_db(self) -> None:
        for word in self.total_composition_words:
            if len(word) == 1 and is_chinese_character(word):
                if not self._user_frequency_db.word_exists(word):
                    self._user_frequency_db.insert(None, word, 1)
                else:
                    self._user_frequency_db.increment_word_frequency(word)

    def update_user_phrase_db(self, text: str) -> None:
        """
        Update the user phrase database with the given phrase and frequency.

        Args:
            phrase (str): The phrase to update
            frequency (int): The frequency of the phrase
        """

        for phrase in jieba.lcut(text, cut_all=False):
            if len(phrase) < 2:
                continue

            if not self._user_phrase_db.getphrase(phrase):
                self._user_phrase_db.insert(phrase, 1)
            else:
                self._user_phrase_db.increment_frequency(phrase)

    def new_reconstruct(self, keystroke: str, top_n: int = 10) -> list[list[str]]:
        class SentenceGraph:
            def __init__(self) -> None:
                self._graph = {}

            @property
            def num_of_node(self) -> int:
                return len(self._graph)

            def add_edge(
                self, u_id: str, v_id: str, distance: int, direct: bool = True
            ) -> None:
                if u_id not in self._graph:
                    self._graph[u_id] = [(v_id, distance)]
                else:
                    if (v_id, distance) not in self._graph[u_id]:
                        self._graph[u_id].append((v_id, distance))

                if v_id not in self._graph:
                    if direct:
                        self._graph[v_id] = []
                    else:
                        self._graph[v_id] = [(u_id, distance)]

            def find_shortest_paths(self, start_id: str, end_id: str) -> list[str]:
                # By Dijkstra
                predcessor = {id: None for id in self._graph}
                distance = {id: None for id in self._graph}
                distance[start_id] = 0

                priorty_queue = [(0, start_id)]
                while priorty_queue:
                    current_distance, current_id = heapq.heappop(priorty_queue)

                    for neighbor_id, neighbor_weight in self._graph[current_id]:
                        neg_new_distance = current_distance + neighbor_weight

                        if distance[neighbor_id] is None:
                            distance[neighbor_id] = neg_new_distance
                            heapq.heappush(
                                priorty_queue, (neg_new_distance, neighbor_id)
                            )
                            predcessor[neighbor_id] = set([current_id])
                        else:

                            if neg_new_distance < distance[neighbor_id]:
                                distance[neighbor_id] = neg_new_distance
                                heapq.heappush(
                                    priorty_queue, (neg_new_distance, neighbor_id)
                                )
                                predcessor[neighbor_id] = set([current_id])
                            elif neg_new_distance == distance[neighbor_id]:
                                predcessor[neighbor_id].add(current_id)

                # Get the path
                def get_path(
                    predcessor: dict[str, set], end_id: str
                ) -> list[list[str]]:

                    def dfs(current_id: str) -> list[list[str]]:
                        if current_id == start_id:
                            return [[start_id]]

                        if predcessor[current_id] is None:
                            return []

                        paths = []
                        for pred in predcessor[current_id]:
                            paths.extend([path + [current_id] for path in dfs(pred)])
                        return paths

                    return dfs(end_id)

                return get_path(predcessor, end_id)

        if not keystroke:
            return []

        # Get all possible seps
        possible_seps = []
        for ime_type in self.actived_imes:
            token_ways = self.ime_handlers[ime_type].tokenize(keystroke)
            possible_seps.extend(token_ways)

        # Filte out empty sep
        possible_seps = [sep for sep in possible_seps if sep]
        # Filter out same sep
        possible_seps = [list(t) for t in set(tuple(token) for token in possible_seps)]

        token_pool = set([token for sep in possible_seps for token in sep])
        new_possible_seps = []
        for sep in possible_seps:
            new_sep = []
            for token in sep:
                is_sep = False
                for i in range(1, len(token)):
                    if token[:i] in token_pool:
                        new_sep.extend([token[:i], token[i:]])
                        is_sep = True
                        break
                if not is_sep:
                    new_sep.append(token)

            new_possible_seps.append(new_sep)
        new_possible_seps.extend(possible_seps)

        self.logger.info(f"Creating Graph with {len(new_possible_seps)} possible seps")
        id_maps = {}
        graph = SentenceGraph()
        for sep in new_possible_seps:
            prev_str = ""
            prev_token_id = "<start>"
            for token in sep:
                empty_token_id = f"<none>_{len(prev_str)}_{len(prev_str)}"
                token_id = f"{token}_{len(prev_str)}_{len(prev_str + token)}"  # Hash it

                id_maps[token_id] = token
                graph.add_edge(prev_token_id, empty_token_id, 0)
                graph.add_edge(empty_token_id, token_id, self.get_token_distance(token))
                prev_str += token
                prev_token_id = token_id
            graph.add_edge(prev_token_id, "<end>", 0)

        shortest_paths = graph.find_shortest_paths("<start>", "<end>")
        self.logger.info(f"Found {len(shortest_paths)} shortest paths")

        possible_paths = []
        for path in shortest_paths:
            path = list(
                filter(
                    lambda x: x not in ["<start>", "<end>"]
                    and not x.startswith("<none>"),
                    path,
                )
            )
            possible_paths.append([id_maps[id] for id in path])
        possible_paths = sorted(possible_paths, key=lambda x: len(x), reverse=False)

        return possible_paths[:top_n]

    @lru_cache_with_doc(maxsize=128)
    def get_token_distance(self, token: str) -> int:
        min_distance = float("inf")

        for ime_type in self.actived_imes:
            if not self.ime_handlers[ime_type].is_valid_token(token):
                continue

            method_distance = self.ime_handlers[ime_type].closest_word_distance(token)
            min_distance = min(min_distance, method_distance)
        return min_distance

    def old_phase1(self, keystroke: str) -> list[str]:
        self.unfreezed_keystrokes = keystroke
        self._update_token_pool()
        possible_sentences = self._reconstruct_sentence_from_pre_possible_sentences(
            self.unfreezed_keystrokes
        )
        possible_sentences = self._sort_possible_sentences(possible_sentences)
        return possible_sentences

    def end_to_end(self, keystroke: str) -> list[str]:
        token_sentences = self.new_reconstruct(keystroke)
        if not token_sentences:
            return []
        return self._token_sentence_to_word_sentence(token_sentences[0])

    def _slow_handle_v2(self):
        token_sentences = self.new_reconstruct(self.unfreezed_keystrokes)
        if not token_sentences:
            return
        self.unfreezed_token_sentence = token_sentences[0]
        self.unfreezed_composition_words = self._token_sentence_to_word_sentence(
            self.unfreezed_token_sentence
        )

if __name__ == "__main__":
    handler = KeyEventHandler()
    phase1_result = handler.old_phase1("zuekua jwjc yk6hqgdi factories")
    new_result = handler.new_reconstruct("zuekua jwjc yk6hqgdi factories")
    print("---------------------")
    print("PHASE1", phase1_result)
    print("NEW", new_result)
    print("---------------------")
    print("PHASE1", handler._calculate_sentence_distance(phase1_result[0]))
    print("NEW", handler._calculate_sentence_distance(new_result[0]))
    print("---------------------")
