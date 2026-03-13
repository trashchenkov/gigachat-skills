---
name: gigachat-sdk-files-embeddings
description: >-
  Uses the official GigaChat Python SDK for file storage, multimodal inputs, and
  text embeddings. Use when uploading documents or images, downloading generated
  assets, or building retrieval systems with embeddings directly on top of the
  gigachat package.
---

# GigaChat SDK Files And Embeddings

Use this skill for storage and vector workflows in the official SDK.

## What this skill covers

- file upload, listing, download, delete
- supported file types and practical size limits
- multimodal workflows that depend on stored file IDs
- embeddings requests and model choice
- batching guidance for embeddings

## Workflow

1. If the task is pure text generation, use `gigachat-sdk-chat` instead.
2. For files, upload first and work with returned file IDs.
3. In one model request, attach files of only one modality. Do not mix images, audio, and documents in the same request.
4. For generated images or 3D assets, fetch content through the files API.
5. For retrieval, pick the embeddings model first, then batch requests sensibly.
6. If the user is actually building LangChain RAG, switch to `langchain-gigachat`.
7. Prefer the simplest verified single-file or embeddings pattern before expanding to more complex workflows.

## Read these references as needed

- For file lifecycle and multimodal notes: `references/files.md`
- For embeddings usage and retrieval notes: `references/embeddings.md`

## Default output

- treat one-modality-per-request as a hard constraint
- use verified single-file or multi-image patterns before suggesting broader multimodal behavior
- separate file lifecycle guidance from embeddings guidance
