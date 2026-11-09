from abc import ABC, abstractmethod


# ───────────────── 1. FACTORY METHOD ─────────────────
class Parser(ABC):
    @abstractmethod
    def parse(self, path: str) -> str: ...


class PDFParser(Parser):
    def parse(self, path: str) -> str:
        return f"[PDF парсері] '{path}' файлы оқылды"


class DocxParser(Parser):
    def parse(self, path: str) -> str:
        return f"[DOCX парсері] '{path}' файлы оқылды"


class DocumentProcessor(ABC):
    @abstractmethod
    def create_parser(self) -> Parser:  # Factory Method
        ...

    def process(self, path: str) -> str:
        parser = self.create_parser()
        return parser.parse(path)


class PDFProcessor(DocumentProcessor):
    def create_parser(self) -> Parser:
        return PDFParser()


class DocxProcessor(DocumentProcessor):
    def create_parser(self) -> Parser:
        return DocxParser()


# ───────────────── 2. ADAPTER ─────────────────
class OldPaymentGate:
    def make_payment(self, cents: int):
        print(f"Ескі шлюз: {cents} цент төленді")


class PaymentAdapter:
    def __init__(self, gate: OldPaymentGate):
        self._gate = gate

    def pay(self, dollars: float):
        cents = round(dollars * 100)  # float қатесін болдырмау үшін round
        self._gate.make_payment(cents)


# ───────────────── 3. DECORATOR ─────────────────
class Report(ABC):
    @abstractmethod
    def render(self) -> str: ...


class TextReport(Report):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text


class ReportDecorator(Report):
    def __init__(self, wrapped: Report):
        self._wrapped = wrapped


class UpperDecorator(ReportDecorator):
    def render(self) -> str:
        return self._wrapped.render().upper()


class HTMLWrapDecorator(ReportDecorator):
    def render(self) -> str:
        return f"<div>{self._wrapped.render()}</div>"


# ───────────────── ДЕМО ─────────────────
if __name__ == "__main__":
    print("--- Factory Method ---")
    for proc, f in [(PDFProcessor(), "a.pdf"), (DocxProcessor(), "b.docx")]:
        print(proc.process(f))

    print("\n--- Adapter ---")
    PaymentAdapter(OldPaymentGate()).pay(12.34)

    print("\n--- Decorator ---")
    base = TextReport("Сәлем, әлем")
    print(UpperDecorator(base).render())
    print(HTMLWrapDecorator(base).render())
    print(HTMLWrapDecorator(UpperDecorator(base)).render())
