"use client";

import { useState, useRef, useEffect } from "react";
import { Send, Code, History, ArrowUpRight, ChevronLeft, ChevronRight } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { useToast } from "@/components/ui/use-toast";
import { ExecutionSteps } from "@/components/ui/execution-steps";
import { ExecutionStepsMinimal } from "@/components/ui/execution-steps-minimal";
import { ChatMessage } from "@/components/ChatMessage";
import { TypingIndicator } from "@/components/TypingIndicator";
import { Header } from "@/components/Header";
import { Resizable } from "@/components/Resizable";

interface Message {
  role: "user" | "assistant";
  content: string;
}

interface ExecutionStep {
  id: number;
  type: 'llm_call' | 'tool_call';
  timestamp: string;
  status: 'success' | 'error';
  input: any;
  output?: string;
  error?: string;
  tool?: string;
  tool_id?: string;
  tool_calls?: Array<{name: string; args: any}>;
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Hello! I'm an AI assistant for {{ project_name }}. How can I help you today?",
    },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [executionSteps, setExecutionSteps] = useState<ExecutionStep[]>([]);
  const [isStepsVisible, setIsStepsVisible] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const { toast } = useToast();

  // Scroll to bottom whenever messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user message to state
    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      // Send API request
      const res = await fetch("/api/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: input,
          conversation_id: conversationId,
        }),
      });

      if (!res.ok) {
        throw new Error(`Error: ${res.status}`);
      }

      const data = await res.json();

      // Update conversation ID if not set
      if (!conversationId) {
        setConversationId(data.conversation_id);
      }

      // Update execution steps if available
      if (data.metadata && data.metadata.execution_steps) {
        setExecutionSteps(data.metadata.execution_steps);
        // Ensure execution steps panel is visible when new steps arrive
        setIsStepsVisible(true);
      }

      // Add response to messages
      const assistantMessage: Message = {
        role: "assistant",
        content: data.response,
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error("Error:", error);
      toast({
        title: "Error",
        description: "Failed to get a response. Please try again.",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const toggleStepsVisibility = () => {
    setIsStepsVisible(!isStepsVisible);
  };

  return (
    <>
      <Header />
      <main className="flex-1 container p-4 md:py-6">
        <div className="h-[calc(100vh-12rem)]">
          <Card className="shadow-sm border-muted/40 h-full flex flex-col">
            <CardHeader className="py-3 px-4 flex flex-row items-center justify-between border-b">
              <CardTitle className="text-xl">Chat</CardTitle>
              <Button
                variant="ghost"
                size="icon"
                onClick={toggleStepsVisibility}
                className="md:hidden"
                aria-label={isStepsVisible ? "Hide execution steps" : "Show execution steps"}
              >
                {isStepsVisible ? <ChevronRight className="h-5 w-5" /> : <ChevronLeft className="h-5 w-5" />}
              </Button>
            </CardHeader>

            <CardContent className="p-0 flex-1 overflow-hidden">
              {/* Desktop: Resizable layout */}
              <div className="h-full hidden md:block">
                <Resizable
                  defaultSize={25}
                  minSize={20}
                  maxSize={40}
                  side="left"
                >
                  {/* Left Side: Execution Steps Panel */}
                  <Card className="rounded-none border-0 border-r h-full flex flex-col bg-muted/10">
                    <CardHeader className="py-2 px-3">
                      <CardTitle className="text-sm flex items-center gap-2">
                        <Code className="h-3.5 w-3.5" />
                        Execution Steps
                      </CardTitle>
                    </CardHeader>
                    <CardContent className="p-0 flex-1 overflow-hidden border-t">
                      <ScrollArea className="h-full">
                        <div className="p-2">
                          {executionSteps.length > 0 ? (
                            <ExecutionStepsMinimal steps={executionSteps} />
                          ) : (
                            <div className="text-muted-foreground text-center py-8">
                              <History className="mx-auto h-6 w-6 mb-2 opacity-40" />
                              <p className="text-xs">No steps recorded yet</p>
                            </div>
                          )}
                        </div>
                      </ScrollArea>
                    </CardContent>
                  </Card>

                  {/* Right Side: Chat Panel */}
                  <div className="h-full flex flex-col">
                    <div className="flex-1 overflow-hidden">
                      <ScrollArea className="h-full">
                        <div className="flex flex-col gap-6 p-4 md:p-6">
                          {messages.map((message, index) => (
                            <ChatMessage
                              key={index}
                              content={message.content}
                              role={message.role}
                            />
                          ))}
                          {isLoading && <TypingIndicator />}
                          <div ref={messagesEndRef} />
                        </div>
                      </ScrollArea>
                    </div>

                    <div className="p-4 pt-2 border-t">
                      <form
                        onSubmit={(e) => {
                          e.preventDefault();
                          handleSend();
                        }}
                        className="flex w-full gap-2"
                      >
                        <Input
                          placeholder="Type your message..."
                          value={input}
                          onChange={(e) => setInput(e.target.value)}
                          onKeyDown={handleKeyDown}
                          disabled={isLoading}
                          className="border-muted/60 focus-visible:ring-primary/30"
                        />
                        <Button
                          disabled={isLoading}
                          type="submit"
                          size="icon"
                          className="shrink-0"
                        >
                          <Send className="h-4 w-4" />
                        </Button>
                      </form>
                    </div>
                  </div>
                </Resizable>
              </div>

              {/* Mobile: Stack layout */}
              <div className="h-full md:hidden">
                {isStepsVisible ? (
                  <div className="h-full flex flex-col">
                    <div className="p-3 border-b flex items-center justify-between">
                      <div className="text-sm font-medium flex items-center gap-2">
                        <Code className="h-3.5 w-3.5" />
                        Execution Steps
                      </div>
                      <Button
                        variant="ghost"
                        size="sm"
                        onClick={toggleStepsVisibility}
                        className="h-7 px-2"
                      >
                        <span className="sr-only">Show chat</span>
                        <ChevronRight className="h-4 w-4" />
                      </Button>
                    </div>
                    <ScrollArea className="flex-1">
                      <div className="p-2">
                        {executionSteps.length > 0 ? (
                          <ExecutionStepsMinimal steps={executionSteps} />
                        ) : (
                          <div className="text-muted-foreground text-center py-8">
                            <History className="mx-auto h-6 w-6 mb-2 opacity-40" />
                            <p className="text-xs">No steps recorded yet</p>
                          </div>
                        )}
                      </div>
                    </ScrollArea>
                  </div>
                ) : (
                  <div className="h-full flex flex-col">
                    <div className="flex-1 overflow-hidden">
                      <ScrollArea className="h-full">
                        <div className="flex flex-col gap-6 p-4">
                          {messages.map((message, index) => (
                            <ChatMessage
                              key={index}
                              content={message.content}
                              role={message.role}
                            />
                          ))}
                          {isLoading && <TypingIndicator />}
                          <div ref={messagesEndRef} />
                        </div>
                      </ScrollArea>
                    </div>

                    <div className="p-4 pt-2 border-t">
                      <form
                        onSubmit={(e) => {
                          e.preventDefault();
                          handleSend();
                        }}
                        className="flex w-full gap-2"
                      >
                        <Input
                          placeholder="Type your message..."
                          value={input}
                          onChange={(e) => setInput(e.target.value)}
                          onKeyDown={handleKeyDown}
                          disabled={isLoading}
                          className="border-muted/60 focus-visible:ring-primary/30"
                        />
                        <Button
                          disabled={isLoading}
                          type="submit"
                          size="icon"
                          className="shrink-0"
                        >
                          <Send className="h-4 w-4" />
                        </Button>
                      </form>
                    </div>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </>
  );
}
