import { useState } from "react";

const API = import.meta.env.VITE_BACKEND_URL;

export default function App() {
  const [text, setText] = useState("");
  const [answer, setAnswer] = useState("");

  async function send() {
    const res = await fetch(`${API}/api/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
    const data = await res.json();
    setAnswer(data.answer);
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>ComplyAI</h1>
      <textarea
        rows="4"
        style={{ width: "100%" }}
        onChange={e => setText(e.target.value)}
      />
      <br /><br />
      <button onClick={send}>Ask</button>
      <pre>{answer}</pre>
    </div>
  );
}
