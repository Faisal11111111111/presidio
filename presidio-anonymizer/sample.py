from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

engine = AnonymizerEngine()

result = engine.anonymize(
    text="My name is Faisal, Faisal Abusara",
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=17, score=0.8),   # Faisal
        RecognizerResult(entity_type="PERSON", start=19, end=33, score=0.8),  # Faisal Abusara
    ],
    operators={"PERSON": OperatorConfig("replace", {"new_value": "Faisal11111111111"})},
)

print(result)
