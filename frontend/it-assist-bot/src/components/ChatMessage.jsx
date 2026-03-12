export default function ChatMessage({ message, isUser }) {
  return (
    <div className={`message ${isUser ? "user-message" : "bot-message"}`}>
      <div className="message-content">
        <p>{message.text}</p>
        {message.context && message.context.length > 0 && (
          <div className="context">
            <strong>Source:</strong>
            {message.context.map((chunk, idx) => (
              <p key={idx} className="context-chunk">
                {chunk.substring(0, 100)}...
              </p>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}