import { useState } from 'react'
import { predictDisease } from '../services/api'

export default function DiseaseDetection() {
  const [file, setFile] = useState(null)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const analyze = async () => {
    if (!file) return setError('Please select a leaf image.')
    setLoading(true); setError(''); setResult(null)
    try { setResult(await predictDisease(file)) }
    catch (e) { setError(e.response?.data?.detail || 'Disease prediction failed.') }
    finally { setLoading(false) }
  }

  return <section className="card">
    <h2>🌿 Disease Detection</h2>
    <p className="muted">Upload a crop leaf image for the MVP classifier.</p>
    <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
    <button onClick={analyze} disabled={loading}>{loading ? 'Analyzing...' : 'Analyze Disease'}</button>
    {error && <p className="error">{error}</p>}
    {result && <div className="result"><strong>{result.disease}</strong><span>Confidence: {(result.confidence * 100).toFixed(0)}%</span></div>}
  </section>
}
