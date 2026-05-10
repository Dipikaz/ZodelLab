import Plot from 'react-plotly.js';

function PlotCanvas({ plotData }) {
  return (
    <Plot
      data={plotData.data}
      layout={{ ...plotData.layout, autosize: true }}
      useResizeHandler={true}
      style={{ width: "100%", height: "100%" }}
    />
  );
}