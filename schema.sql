CREATE TABLE public."Responses" (
	"ResponseId" serial4 NOT NULL,
	"Key" varchar(255) NOT NULL,
	"Model" varchar(255) NOT NULL,
	"ClientPrompt" text NULL,
	"CreatedAt" timestamp DEFAULT CURRENT_TIMESTAMP NULL,
	"UpdatedAt" timestamp NULL,
	"Query" text NULL,
	CONSTRAINT responses_pk PRIMARY KEY ("ResponseId"),
	CONSTRAINT responses_unique UNIQUE ("Key")
);