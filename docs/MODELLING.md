# OpenAI API Architecture

This document outlines the architecture for interacting with the OpenAI API, detailing the major components, their descriptions, and the actions associated with each component.

## Major Components

### Assistants

Build Assistants that can call models and use tools.

- `listAssistants()`
- `createAssistant()`
- `getAssistant()`
- `modifyAssistant()`
- `deleteAssistant()`
- `createThread()`
- `getThread()`
- `modifyThread()`
- `deleteThread()`
- `listMessages()`
- `createMessage()`
- `getMessage()`
- `modifyMessage()`
- `createThreadAndRun()`
- `listRuns()`
- `createRun()`
- `getRun()`
- `modifyRun()`
- `submitToolOutputsToRun()`
- `cancelRun()`
- `listRunSteps()`
- `getRunStep()`
- `listAssistantFiles()`
- `createAssistantFile()`
- `getAssistantFile()`
- `deleteAssistantFile()`
- `listMessageFiles()`
- `getMessageFile()`

### Audio

Learn how to turn audio into text or text into audio.

- `createSpeech()`
- `createTranscription()`
- `createTranslation()`

### Chat

Given a list of messages comprising a conversation, the model will return a response.

- `createChatCompletion()`

### Completions

Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.

- `createCompletion()`

### Embeddings

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

- `createEmbedding()`

### Fine-tuning

Manage fine-tuning jobs to tailor a model to your specific training data.

- `createFineTuningJob()`
- `listPaginatedFineTuningJobs()`
- `retrieveFineTuningJob()`
- `listFineTuningEvents()`
- `cancelFineTuningJob()`

### Files

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

- `listFiles()`
- `createFile()`
- `deleteFile()`
- `retrieveFile()`
- `downloadFile()`

### Images

Given a prompt and/or an input image, the model will generate a new image.

- `createImage()`
- `createImageEdit()`
- `createImageVariation()`

### Models

List and describe the various models available in the API.

- `listModels()`
- `retrieveModel()`
- `deleteModel()`

### Moderations

Given an input text, outputs if the model classifies it as violating OpenAI's content policy.

- `createModeration()`

### Fine-tunes

Manage legacy fine-tuning jobs to tailor a model to your specific training data.

- `createFineTune()`
- `listFineTunes()`
- `retrieveFineTune()`
- `cancelFineTune()`
- `listFineTuneEvents()`

### Edits

Given a prompt and an instruction, the model will return an edited version of the prompt.

- `createEdit()`
