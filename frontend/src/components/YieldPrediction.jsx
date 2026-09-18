import { useState } from 'react'
import { predictYield } from '../services/api'

const initial = { crop_name: 'Rice', soil_ph: 6.5, temperature: 28, rainfall: 850, humidity: 75, soil_moisture: 62, area: 2 }

export default function YieldPrediction({ onDone }) {
  const [form, setForm] = useState(initial)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const update = (key, value) => setForm({...form, [key]: key === 'crop_name' ? value : Number(value)})
  const submit = async e => {
    e.preventDefault(); setLoading(true); setError(''); setResult(null)
    try { const r = await predictYield(form); setResult(r); onDone?.() }
    catch (e) { setError(e.response?.data?.detail || 'Yield prediction failed.') }
    finally { setLoading(false) }
  }
  return <section className="card">
    <h2>📈 Yield Prediction</h2>
    <p className="muted">Enter basic crop and environmental values.</p>
    <form onSubmit={submit} className="form-grid">
      <label>Crop<select value={form.crop_name} onChange={e => update('crop_name', e.target.value)}>{['Rice','Wheat','Maize','Tomato','Potato','Cotton'].map(x => <option key={x}>{x}</option>)}</select></label>
      <label>Soil pH<input type="number" step="0.1" value={form.soil_ph} onChange={e => update('soil_ph', e.target.value)}/></label>
      <label>Temperature °C<input type="number" value={form.temperature} onChange={e => update('temperature', e.target.value)}/></label>
      <label>Rainfall mm<input type="number" value={form.rainfall} onChange={e => update('rainfall', e.target.value)}/></label>
      <label>Humidity %<input type="number" value={form.humidity} onChange={e => update('humidity', e.target.value)}/></label>
      <label>Soil moisture %<input type="number" value={form.soil_moisture} onChange={e => update('soil_moisture', e.target.value)}/></label>
      <label>Area (acres)<input type="number" step="0.1" value={form.area} onChange={e => update('area', e.target.value)}/></label>
      <button type="submit" disabled={loading}>{loading ? 'Predicting...' : 'Predict Yield'}</button>
    </form>
    {error && <p className="error">{error}</p>}
    {result && <div className="result"><strong>{result.predicted_yield} tons</strong><span>Estimated crop yield</span></div>}
  </section>
}
