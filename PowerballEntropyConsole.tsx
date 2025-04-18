import { useState } from 'react'

export default function PowerballEntropyConsole() {
  const [inputData, setInputData] = useState('')
  const [sessionHistory, setSessionHistory] = useState('pass,fail')
  const [result, setResult] = useState<any | null>(null)
  const [loading, setLoading] = useState(false)

  const handleDraw = async () => {
    setLoading(true)
    setResult(null)

    const payload = {
      input_data: inputData,
      session_history: sessionHistory.split(',').map(s => 
s.trim()),
      timestamps: Array(sessionHistory.split(',').length)
        .fill(0)
        .map((_, i) => Date.now() + i * 1000)
    }

    try {
      const res = await 
fetch('http://localhost:5050/api/edao/gateway', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      const data = await res.json()
      setResult(data)
    } catch (err) {
      console.error('Error contacting Precision eDAO Gateway:', 
err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-3xl mx-auto p-6 text-white">
      <h1 className="text-2xl font-bold mb-4 text-indigo-400">🎴 
Precision eDAO Gateway</h1>

      <div className="mb-4">
        <label className="block mb-1">🔤 Input Symbolic 
String</label>
        <input
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
          className="w-full p-2 bg-gray-800 border border-gray-700 
rounded"
        />
      </div>

      <div className="mb-4">
        <label className="block mb-1">📜 Session History 
(comma-separated: pass,fail,...)</label>
        <input
          value={sessionHistory}
          onChange={(e) => setSessionHistory(e.target.value)}
          className="w-full p-2 bg-gray-800 border border-gray-700 
rounded"
        />
      </div>

      <button
        onClick={handleDraw}
        className="bg-indigo-600 hover:bg-indigo-700 text-white 
px-6 py-2 rounded shadow"
      >
        🎲 Run Karmic Draw
      </button>

      {loading && <p className="mt-4 text-gray-400">Drawing...</p>}

      {result && (
        <div className="mt-6 bg-gray-900 p-4 rounded shadow">
          <h2 className="text-lg font-bold text-indigo-300 mb-2">🎯 
Draw Results</h2>
          <div className="grid grid-cols-2 gap-2 text-sm">
            {Object.entries(result).map(([key, val]) => (
              <div key={key} className="flex justify-between py-1 
border-b border-gray-800">
                <span className="text-gray-400">{key}</span>
                <span className="font-mono 
text-green-400">{String(val)}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

