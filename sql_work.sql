USE clean_winery;

SELECT wine_name, varietal_name, country, wine_id, type, style_id FROM wine
JOIN style USING(wine_id)
JOIN purchase USING (wine_id)
WHERE style_id != body
ORDER BY style_id;

SELECT * FROM style;
SELECT * FROM purchase;

SELECT wine_id, type, wine_name, country, varietal_name, IFNULL(style_id, 0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM wine
LEFT JOIN purchase USING (wine_id)
LEFT JOIN  style USING (wine_id)
WHERE (wine_name LIKE '%Garnacha%') OR (wine_name LIKE '%%Garnatxa%%');

SELECT wine_id, type, wine_name, country, varietal_name, IFNULL(style_id, 0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM wine
LEFT JOIN purchase USING (wine_id)
LEFT JOIN  style USING (wine_id)
ORDER BY style_id;

SELECT wine_id, type, wine_name, country, IFNULL(varietal_name, 'Moscatel') AS varietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM wine
LEFT JOIN purchase USING (wine_id)
LEFT JOIN  style USING (wine_id)
WHERE wine_name LIKE '%%Moscatel%%';

SELECT wine_id, type, wine_name, country, varietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM wine
LEFT JOIN purchase USING (wine_id)
LEFT JOIN  style USING (wine_id)
WHERE wine_name LIKE '%Sauvignon Blanc - Muscat%';

SELECT wine_id, w.type, w.wine_name, w.country, varietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM wine w
JOIN to_clean_2 USING (wine_id)
WHERE region LIKE '%Ribeiro%';

SELECT wine_id, type, wine_name, country, varietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM to_clean_2
WHERE wine_name LIKE '%Ribeiro%';

SELECT wine_id, type, wine_name, country, varietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM to_clean_2
WHERE wine_name LIKE "%Tempranillo%";

SELECT wine_id, type, wine_name, country, (varietal_name = '%Merlot - Syrah%') AS varietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM wine
LEFT JOIN purchase USING (wine_id)
LEFT JOIN  style USING (wine_id)
WHERE wine_name LIKE '%Merlot - Syrah%';

SELECT wine_id, type, wine_name, country, IFvarietal_name, IFNULL(style_id,0) AS style_id, body, acidity_1, acidity_2, fizziness, intensity, sweetness, tannin FROM to_clean_2
WHERE type = 1;
-- WHERE (wine_name LIKE '%Tinto%') OR (wine_name LIKE '%Red%') OR (wine_name LIKE '%Rouge%') ;


SELECT d.wine_id, d.type, d.wine_name, d.country, w.region, d.varietal_name, w.winery, w.year, d.style_id, d.body, d.acidity_1, s.acidity_description, d.acidity_2, d.fizziness, d.intensity, d.sweetness, d.tannin, p.vol_ml, p.price_eur, w.num_ratings, w.rate FROM df_to_clean d
LEFT JOIN wine w USING (wine_id)
LEFT JOIN purchase p USING (wine_id)
LEFT JOIN style s USING (wine_id);

SELECT varietal_name, COUNT(wine_id) AS count FROM all_data
WHERE varietal_name LIKE '%Vino espumoso%'
GROUP BY varietal_name
ORDER BY COUNT(wine_id) DESC;

SELECT type, country, region, varietal_name FROM data_to_model
GROUP BY varietal_name
ORDER BY varietal_name;

SELECT type, country, region, varietal_name FROM data_to_model
WHERE varietal_name LIKE '%Hermitage%';

SELECT country, region, varietal_name, COUNT(type) AS count FROM data_to_model
GROUP BY varietal_name
ORDER BY count;

DROP TABLE IF EXISTS to_clean;

DROP TABLE IF EXISTS to_clean_2;

DROP TABLE IF EXISTS clustered;

DROP TABLE IF EXISTS godello_demo;

DROP TABLE IF EXISTS df_to_clean;

SELECT c.wine_id, w.wine_name, w.winery, c.region, c.country, c.varietal_name, c.type, c.year, c.style_id, c.body, c.acidity_1, c.acidity_description, c.acidity_2, c.fizziness, c.intensity, c.sweetness, c.tannin, c.clusters, p.vol_ml, p.price_eur, c.num_ratings, c.rate FROM clustered c
LEFT JOIN wine w USING (wine_id)
LEFT JOIN purchase p USING (wine_id)
LEFT JOIN style s USING (wine_id);

SELECT wine_id, wine_name, winery, region, country, varietal_name, type, year, vol_ml, price_eur, num_ratings, rate FROM  all_data;

SELECT body, SUM(intensity), SUM(sweetness),SUM(tannin) FROM clustered
GROUP BY body
ORDER BY body;

SELECT * FROM clustered