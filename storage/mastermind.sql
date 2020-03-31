PRAGMA foreign_keys = OFF;

-- Schema: mastermind
BEGIN;
DROP TABLE IF EXISTS "game";
CREATE TABLE "game"(
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "player_name" VARCHAR(45) NOT NULL,
  "created_at" TIMESTAMP NOT NULL,
  "completed_at" TIMESTAMP,
  "code" TEXT NOT NULL,
  "color_options" TEXT NULL,
  "double_colors" INTEGER NOT NULL,
  "amount_of_colors" INTEGER NOT NULL,
  "amount_of_positions" INTEGER NOT NULL
);
DROP TABLE IF EXISTS "game_turn";
CREATE TABLE "game_turn"(
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "game_id" INTEGER NOT NULL,
  "submitted_at" TIMESTAMP NOT NULL,
  "code_guessed" VARCHAR(45) NOT NULL,
  CONSTRAINT "fk_game_turn_game1"
    FOREIGN KEY("game_id")
    REFERENCES "game"("id")
);
CREATE INDEX "game_turn.fk_game_turn_game1_idx" ON "game_turn" ("game_id");
COMMIT;