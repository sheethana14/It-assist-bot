import { useState, useRef, useEffect } from "react";
import { sendChat } from "../services/api";
import ChatMessage from "./ChatMessage";

export default function ChatBox({ documentUploaded }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim() || !documentUploaded) {
      alert("Please upload a PDF first");
      return;
    }

    const userMessage = input;
    setInput("");
    setMessages((prev) => [...prev, { text: userMessage, isUser: true }]);
    setLoading(true);

    try {
      const response = await sendChat(userMessage);
      setMessages((prev) => [
        ...prev,
        {
          text: response.response,
          context: response.context,
          isUser: false,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { text: `Error: ${error.message}`, isUser: false },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-box">
      <div className="messages">
        {messages.length === 0 && (
          <p className="empty-state">Upload a PDF and start asking questions!</p>
        )}
        {messages.map((msg, idx) => (
          <ChatMessage
            key={idx}
            message={msg}
            isUser={msg.isUser}
          />
        ))}
        {loading && <p className="loading">Bot is typing...</p>}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSendMessage} className="chat-input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          disabled={!documentUploaded || loading}
        />
        <button type="submit" disabled={!documentUploaded || loading}>
          Send
        </button>
      </form>
    </div>
  );
}