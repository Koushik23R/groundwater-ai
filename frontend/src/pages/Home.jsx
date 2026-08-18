import { useEffect, useState } from 'react'
import { getHealth } from '../services/api'

function Home() {
  const [connection, setConnection] = useState({
    loading: true,
    connected: false,
    message: 'Checking backend connection...',
  })

  useEffect(() => {
    let isMounted = true

    const checkHealth = async () => {
      try {
        const data = await getHealth()

        if (isMounted) {
          setConnection({
            loading: false,
            connected: data?.status === 'ok',
            message: data?.status === 'ok' ? 'Backend connected' : 'Backend unavailable',
          })
        }
      } catch {
        if (isMounted) {
          setConnection({
            loading: false,
            connected: false,
            message: 'Backend unavailable',
          })
        }
      }
    }

    checkHealth()

    return () => {
      isMounted = false
    }
  }, [])

  return (
    <div className="page-shell">
      <header className="page-header">
        <span className="eyebrow">Project Overview</span>
        <h1>Predictive Modeling of Ground Water Depletion and Artificial Recharge Potential</h1>
      </header>

      <div className={`status-banner ${connection.connected ? 'success' : 'warning'}`}>
        {connection.loading ? 'Checking backend connection...' : connection.message}
      </div>

      <p className="lead-text">
        This academic project is designed to analyze historical groundwater-related data,
        predict groundwater levels using a trained machine learning model, present artificial
        recharge potential assessment results, and provide model explainability insights for
        decision support.
      </p>

      <div className="info-grid">
        <article className="info-card">
          <h2>Groundwater prediction</h2>
          <p>Use a trained model to estimate groundwater conditions from historical station data and engineered features.</p>
        </article>

        <article className="info-card">
          <h2>Artificial recharge assessment</h2>
          <p>Review station-level recharge potential results derived from rule-based assessment logic.</p>
        </article>

        <article className="info-card">
          <h2>Model explainability</h2>
          <p>Inspect feature importance and permutation-importance results to understand model behavior and drivers.</p>
        </article>
      </div>
    </div>
  )
}

export default Home
