export default function History({ items }) {
  return <section className="card"><h2>🕘 Prediction History</h2>
    {items.length === 0 ? <p className="muted">No predictions yet.</p> : <div className="history">{items.map(x => <div className="history-row" key={x.id}><span>{x.prediction_type === 'disease' ? '🌿' : '📈'} {x.prediction_type}</span><span>{x.disease || `${x.crop_name}: ${x.predicted_yield} tons`}</span></div>)}</div>}
  </section>
}
