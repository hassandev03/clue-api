# Alan Wake — Clue API

A backend API for the **Clue** entity, the piece of evidence a player uncovers while working a case in the Alan Wake games.

---

## Overview

A "Clue" is a single piece of evidence the player uncovers while working a case. In the Alan Wake games these are the collectibles and story beats that populate the Case Board in the Mind Place: case facts, character profiles, manuscript pages, nursery rhymes, cult stashes, and the like.

This API exposes the Clue entity as a resource so that a front end — the Case Board itself, a companion app, or an admin tool — can read, filter, and curate clues without knowing anything about how they are stored.

---

## The Clue resource

Every clue is represented by the same set of fields.

| Field           | Type      | Required         | Default        | Notes                                                                                        |
| --------------- | --------- | ---------------- | -------------- | -------------------------------------------------------------------------------------------- |
| `id`            | string    | Server-assigned  | —              | Unique identifier. Read-only; generated on create and never changes.                          |
| `title`         | string    | **Yes**          | —              | Short display name, as it appears on the Case Board card. 1–120 characters.                   |
| `description`   | string    | **Yes**          | —              | The full text of the clue as the player reads it. May be long.                                |
| `case_id`       | string    | **Yes**          | —              | Identifier of the case this clue belongs to. Groups clues onto a single Case Board.           |
| `chapter`       | integer   | No               | —              | Which chapter of the story the clue is found in. Used for progression ordering.               |
| `location`      | string    | No               | —              | Where the clue was found. See [locations](#locations).                                        |
| `clue_type`     | string    | No               | `"case_fact"`  | Category of the clue. See [clue types](#clue-types).                                          |
| `discovered`    | boolean   | No               | `false`        | Whether the player has found this clue yet. Drives empty slots on the board.                   |
| `discovered_at` | timestamp | Server-set       | `null`         | When the clue was discovered. Null while `discovered` is `false`.                             |
| `media_url`     | string    | No               | —              | Optional link to an associated image or audio file (a manuscript scan, an Echo recording).    |

### Clue types

`clue_type` accepts one of the following values:

| Value               | Meaning                          |
| ------------------- | -------------------------------- |
| `case_fact`         | Default. A factual case detail.  |
| `profile`           | A character profile.             |
| `manuscript_page`   | A page of the manuscript.        |
| `nursery_rhyme`     | A nursery rhyme clue.            |
| `cult_stash`        | A cult stash.                    |
| `echo`              | An Echo.                         |
| `other`             | Anything that fits no category.  |

### Locations

`location` is a free-text string. The games' canonical settings are:

- Bright Falls
- Watery
- Cauldron Lake
- The Dark Place

---

## Endpoints

| Method   | Path                     | Purpose                          |
| -------- | ------------------------ | -------------------------------- |
| `GET`    | `/clues`                 | List and filter clues            |
| `GET`    | `/clues/search`          | Full-text search                 |
| `GET`    | `/clues/{clue_id}`       | Fetch a single clue              |
| `POST`   | `/clues`                 | Create a clue                    |
| `PUT`    | `/clues/{clue_id}`       | Replace a clue                   |
| `PATCH`  | `/clues/{clue_id}`       | Partially update a clue          |
| `DELETE` | `/clues/{clue_id}`       | Delete a clue                    |
| `GET`    | `/cases/{case_id}/clues` | List the clues belonging to a case |

---

