"use client";

import { Cat } from "lucide-react";

import { Chat } from "@/components/chat";

const ASSISTANT_ID = "simple_agent";

export default function Page() {
  return (
    <main className="flex h-dvh flex-col">
      <header className="border-b bg-background">
        <div className="mx-auto flex w-full max-w-3xl items-center gap-2 px-4 py-3">
          <div className="flex size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
            <Cat className="size-4" />
          </div>
          <div className="leading-tight">
            <p className="text-sm font-medium">Cat Health Agent</p>
            <p className="text-xs text-muted-foreground">LangGraph + Next.js</p>
          </div>
        </div>
      </header>

      <Chat assistantId={ASSISTANT_ID} />
    </main>
  );
}
