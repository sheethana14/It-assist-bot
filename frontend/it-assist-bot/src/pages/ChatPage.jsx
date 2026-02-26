import { useState } from "react";
import { api } from "../services/api";

function ChatPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [topK, setTopK] = useState(3);

  const handleSend = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    try {
      const response = await api.post("/chat", {
        question: input,
        top_k: topK,
        history: messages
          .filter(m => m.role === "assistant")
          .map((m, i) => ({
            question: messages[i * 2]?.content,
            answer: m.content
          }))
      });

      setMessages([
        ...newMessages,
        { role: "assistant", content: response.data.answer }
      ]);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      
      {/* Sidebar */}
      <div style={{
        width: "250px",
        background: "#1e1e1e",
        color: "white",
        padding: "20px"
      }}>
        <h3>Settings</h3>
        <label>Top K:</label>
        <input
          type="number"
          value={topK}
          onChange={(e) => setTopK(Number(e.target.value))}
        />
      </div>

      {/* Chat Area */}
      <div style={{ flex: 1, padding: "20px", display: "flex", flexDirection: "column" }}>
        
        <div style={{ flex: 1, overflowY: "auto" }}>
          {messages.map((msg, index) => (
            <div
              key={index}
              style={{
                textAlign: msg.role === "user" ? "right" : "left",
                marginBottom: "15px"
              }}
            >
              <div style={{
                display: "inline-block",
                padding: "10px",
                borderRadius: "10px",
                background: msg.role === "user" ? "#007bff" : "#e5e5e5",
                color: msg.role === "user" ? "white" : "black",
                maxWidth: "60%"
              }}>
                {msg.content}
              </div>
            </div>
          ))}
          {loading && <p>Thinking...</p>}
        </div>

        <div style={{ display: "flex", marginTop: "10px" }}>
          <input
            style={{ flex: 1, padding: "10px" }}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask something..."
          />
          <button onClick={handleSend}>Send</button>
        </div>

      </div>
    </div>
  );
}

export default ChatPage;