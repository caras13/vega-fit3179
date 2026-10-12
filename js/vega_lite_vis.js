// Chart 1: State Choropleth Map
vegaEmbed('#map_1', 'jsons/map_1_choropleth.json', { "actions": false })
  .then(() => console.log("Chart 1 loaded"))
  .catch(console.error);

// Chart 2: Metro vs Regional Dumbbell
vegaEmbed('#chart_2', 'jsons/chart_2_dumbbell.json', { "actions": false })
  .then(() => console.log("Chart 2 loaded"))
  .catch(console.error);

// Chart 3: NAPLAN Grouped Bar
vegaEmbed('#chart_3', 'jsons/chart_3_grouped_bar.json', { "actions": false })
  .then(() => console.log("Chart 3 loaded"))
  .catch(console.error);

// Map 3: State STEM Dorling Cartogram
vegaEmbed('#map_3', 'jsons/map_3_cartogram.json', { "actions": false })
  .then(function(result) {
    console.log("Map 3 loaded");
  })
  .catch(console.error);

// Chart 4: University Proportional Symbol Map
vegaEmbed('#map_2', 'jsons/map_2_symbols.json', { "actions": false })
  .then(() => console.log("Chart 4 loaded"))
  .catch(console.error);

// Chart 5: Low SES vs High SES Dumbbell
vegaEmbed('#chart_5', 'jsons/chart_5_dumbbell.json', { "actions": false })
  .then(() => console.log("Chart 5 loaded"))
  .catch(console.error);

// Chart 6: Field vs Gender Heatmap
vegaEmbed('#chart_6', 'jsons/chart_6_heatmap.json', { "actions": false })
  .then(() => console.log("Chart 6 loaded"))
  .catch(console.error);

// Chart 7: Pathways Flow Chart
vegaEmbed('#chart_7', 'jsons/chart_7_sankey.json', { "actions": false })
  .then(() => console.log("Chart 7 loaded"))
  .catch(console.error);

// Chart 8: Hexagonal Tile Map
vegaEmbed('#chart_8', 'jsons/chart_8_hexmap.json', { "actions": false })
  .then(() => console.log("Chart 8 loaded"))
  .catch(console.error);

// Chart 9: Discipline Hierarchy Treemap
vegaEmbed('#chart_9', 'jsons/chart_9_treemap.json', { "actions": false })
  .then(() => console.log("Chart 9 loaded"))
  .catch(console.error);

// Chart 10: Graduate Performance Parallel Coordinates Plot
vegaEmbed('#chart_10', 'jsons/chart_10_parallel.json', { "actions": false })
  .then(() => console.log("Chart 10 loaded"))
  .catch(console.error);
// Chart 11: Projected Industry Employment Streamgraph
vegaEmbed('#chart_11', 'jsons/chart_11_streamgraph.json', { "actions": false })
  .then(() => console.log("Chart 11 loaded"))
  .catch(console.error);

// Chart 12: Historical 10-Year Multi-line Plot
vegaEmbed('#chart_12', 'jsons/chart_12_multiline.json', { "actions": false })
  .then(() => console.log("Chart 12 loaded"))
  .catch(console.error);