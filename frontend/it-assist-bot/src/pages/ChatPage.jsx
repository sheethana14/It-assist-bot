import { useState } from "react";
import { api } from "../services/api";

function ChatPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);
      setAnswer("");

      const response = await api.post("/chat", {
        question: question,
        top_k: 3,
      });

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", maxWidth: "600px" }}>
      <h2>Ask IT Assistant</h2>

      <textarea
        rows="4"
        style={{ width: "100%", padding: "10px" }}
        placeholder="Ask your IT question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <br /><br />

      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      <br /><br />

      {answer && (
        <div style={{
          background: "#f5f5f5",
          padding: "15px",
          borderRadius: "8px"
        }}>
          <strong>Answer:</strong>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default ChatPage;