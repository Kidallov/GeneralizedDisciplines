"""Воспроизводимый пример занятия. Распознаватель возвращает учебный черновик."""
from model import Phase, Question, ReadingSession, ReadingTask, Recognizer, Scorer
from scoring import ReadingScorer


class ExampleRecognizer:
    def transcribe(self, audio_ref: str) -> str:
        if audio_ref != "example:reading-01":
            raise ValueError("Неизвестная демонстрационная запись")
        return "Маша увидела у крыльца ерша. Ёж спрятался под кустом."


def run(recognizer: Recognizer, scorer: Scorer) -> ReadingSession:
    task = ReadingTask(
        text="Утром Маша увидела у крыльца ежа. Ёж спрятался под кустом.",
        questions=[
            Question("Кого увидела Маша?", ["Ежа", "Ерша", "Зайца"], 0),
            Question("Куда спрятался ёж?", ["Под крыльцо", "Под куст", "В траву"], 1),
        ],
    )
    session = ReadingSession("example-01", task, Phase.ASSIGNED, None, 0.0, None, [], None)
    session.phase = Phase.RECORDING
    session.audio_ref = "example:reading-01"
    session.seconds = 15.0
    session.phase = Phase.RECOGNIZING
    draft = recognizer.transcribe(session.audio_ref)
    session.transcript = draft
    session.phase = Phase.REVIEW
    print("Черновик:", draft)
    # Воспроизводим подтверждение педагогом и два выбора ребёнка.
    session.transcript = "Маша увидела у крыльца ежа. Ёж спрятался под кустом."
    print("После сверки:", session.transcript)
    session.phase = Phase.QUESTIONS
    session.answers = [0, 0]
    session.result = scorer.evaluate(session)
    session.phase = Phase.COMPLETED
    return session


if __name__ == "__main__":
    session = run(ExampleRecognizer(), ReadingScorer())
    result = session.result
    assert result is not None
    print(f"Расхождения: {result.word_edits} на {result.reference_words} слов эталона")
    print(f"Темп: {result.words_per_minute:g} слов/мин")
    print(f"Понимание: {result.correct} из {result.total}")
    print(f"Статус: {session.phase.value}")
