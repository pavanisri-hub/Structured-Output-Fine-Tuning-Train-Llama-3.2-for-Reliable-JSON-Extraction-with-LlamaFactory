// app/page.tsx (Next.js 13+ app router)
export default function Home() {
  return (
    <main style={{ padding: '2rem', fontFamily: 'system-ui' }}>
      <h1>Structured Output Fine-Tuning: Llama 3.2 JSON Extraction</h1>
      <p>
        This project fine-tunes Llama 3.2 with LoRA using LlamaFactory to reliably
        extract structured JSON from invoices and purchase orders.
      </p>

      <h2>Key Artifacts</h2>
      <ul>
        <li><code>schema/invoice_schema.md</code> and <code>schema/po_schema.md</code> – JSON schemas.</li>
        <li><code>data/curated_train.jsonl</code> – 80 curated training examples.</li>
        <li><code>training_config.md</code> – LoRA hyperparameters and run log.</li>
        <li><code>eval/summary.md</code> – baseline vs fine-tuned metrics.</li>
        <li><code>report.md</code> – analysis and prompting vs fine-tuning discussion.</li>
      </ul>

      <h2>Headline Result</h2>
      <p>
        Parse success rate on 20 held-out documents improved from 55% (baseline)
        to 95% after fine-tuning.
      </p>
    </main>
  );
}