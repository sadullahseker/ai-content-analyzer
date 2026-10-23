# AI Content Analyzer

An automated FastAPI backend service designed to preprocess text data and perform rule-based sentiment analysis. This project provides a structured pipeline for clean text normalization, word count extraction, and sentiment scoring.

## Tech Stack

- Language: Python 3.9+
- Framework: FastAPI
- Data Validation: Pydantic
- Text Processing: Regex

## Key Features

- Fast text normalization and cleaning using Regex
- Word count and length metric extraction
- Rule-based sentiment analysis engine (Positive, Negative, Neutral classification)
- Input payload validation with Pydantic
- Automatic interactive API documentation (Swagger UI)

## API Endpoints

- GET / : Health check endpoint.
- POST /analyze : Accepts text payload and returns sentiment classification, confidence score, word count, and cleaned text.

## License

This project is licensed under the MIT License.
