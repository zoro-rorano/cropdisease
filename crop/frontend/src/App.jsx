import { useEffect, useState } from 'react'
import DiseaseDetection from './components/DiseaseDetection'
import YieldPrediction from './components/YieldPrediction'
import History from './components/History'
import { getHistory } from './services/api'
import './App.css'

export default function App() {
  const [history, setHistory] = useState([])
  const refresh = async () => { try { setHistory(await getHistory()) } catch {} }
  useEffect(() => { refresh() }, [])
  return <main>
    <header><div><span className="eyebrow">SMART CROP AI</span><h1>Crop Disease & Yield Prediction</h1><p>Simple AI-assisted agricultural prediction MVP</p></div></header>
    <div className="container"><div className="grid"><DiseaseDetection/><YieldPrediction onDone={refresh}/></div><History items={history}/></div>
  </main>
}
