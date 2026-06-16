# Files

Use this file for uploads, file-backed prompts, and multimodal requests in the native SDK.

## Default path

1. Upload the local file.
2. Keep the returned `file_id`.
3. Pass that file in `attachments` when the model should inspect it.
4. Keep one request limited to one modality.
5. Download generated assets through the files API when needed.

Status: `smoke-covered`

## Main file operations

- upload file
- list files
- get file metadata
- download file content
- delete file

Status: `smoke-covered`

## Modality rule

Attach files of only one modality per request.

Good:

- image + image
- audio + audio
- document + document

Avoid:

- image + audio
- image + pdf
- audio + pdf

If the application needs multiple modalities, split the work into separate requests and combine results in application code.

Status: `smoke-covered`

## Smoke-covered file-context prerequisites

The lightweight verification scripts cover upload/file-ID prerequisites for:

- single image context
- single audio context
- single PDF context
- multi-image comparison setup

They are smoke checks, not a full semantic benchmark of model understanding. Treat deeper content-understanding claims as source-backed or live-test-specific unless a task runs stronger assertions.

Status: `smoke-covered`

## Known unreliable scenarios

- mixed modalities in one request
- mixed modalities across turns

Status: `caution`

## Size limits

Local docs indicate:

- audio: 35 MB
- image: 15 MB
- text document: 40 MB
- combined audio + image payloads: under 80 MB

Treat these as documented limits, not as smoke-covered guarantees for every endpoint path.

Status: `source-backed`

## Decision rules

- if the model must inspect a document or image, upload first and pass the file ID
- if you need raw bytes for a generated image, use the file-content endpoint
- delete transient files in long-running systems
- multiple images in one request are acceptable for comparison tasks

Status: `smoke-covered`
