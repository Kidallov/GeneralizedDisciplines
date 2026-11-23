"""Расчёт показателей по подтверждённой педагогом расшифровке."""
from math import isfinite
import re

from model import Assessment, Phase, ReadingSession


def words(text: str) -> list[str]:
    """Для учебных текстов: без регистра и пунктуации, ё = е, дефис внутри слова."""
    return re.findall(r"[а-яa-z0-9]+(?:-[а-яa-z0-9]+)*", text.lower().replace("ё", "е"))


def edit_distance(reference: list[str], actual: list[str]) -> int:
    """Минимум вставок, пропусков и замен слов при единичных весах."""
    previous = list(range(len(actual) + 1))
    for row, expected_word in enumerate(reference, 1):
        current = [row]
        for col, spoken_word in enumerate(actual, 1):
            current.append(min(
                current[-1] + 1,
                previous[col] + 1,
                previous[col - 1] + (expected_word != spoken_word),
            ))
        previous = current
    return previous[-1]


class ReadingScorer:
    def evaluate(self, session: ReadingSession) -> Assessment:
        if session.phase != Phase.QUESTIONS or session.transcript is None:
            raise ValueError("Для расчёта нужна утверждённая расшифровка")
        reference = words(session.task.text)
        if not reference or not isfinite(session.seconds) or session.seconds <= 0:
            raise ValueError("Нужны эталонный текст и положительная длительность")
        questions = session.task.questions
        if not questions or len(session.answers) != len(questions):
            raise ValueError("Нужен один ответ на каждый вопрос")
        correct = 0
        for question, answer in zip(questions, session.answers):
            if not (0 <= question.key < len(question.options) and 0 <= answer < len(question.options)):
                raise ValueError("Номер варианта вне списка")
            correct += answer == question.key
        actual = words(session.transcript)
        return Assessment(
            word_edits=edit_distance(reference, actual),
            reference_words=len(reference),
            words_per_minute=len(actual) * 60 / session.seconds,
            correct=correct,
            total=len(questions),
        )
