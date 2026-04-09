# Fine-Tuned Responses

Prompt used for all 20 held-out documents:

Extract all invoice or purchase-order fields and return ONLY a valid JSON object. No explanation, no markdown, no code fences.

## E01.txt
Raw model output:
{"vendor":"Northwind Industrial Supply","invoice_number":"INV-10091","date":"2026-01-03","due_date":"2026-02-02","currency":"USD","subtotal":1600.0,"tax":240.0,"total":1840.0,"line_items":[{"description":"Hydraulic seal kit","quantity":8,"unit_price":200.0}]}

## E02.txt
Raw model output:
{"vendor":"Atlas Precision Tools","invoice_number":"APT-773","date":"2026-01-04","due_date":"2026-02-03","currency":"USD","subtotal":870.0,"tax":60.0,"total":930.0,"line_items":[{"description":"Cutting insert","quantity":30,"unit_price":29.0}]}

## E03.txt
Raw model output:
{"vendor":"Pioneer Mechanical Works","invoice_number":"PMW-44","date":"2026-01-05","due_date":null,"currency":"EUR","subtotal":1100.0,"tax":125.0,"total":1225.0,"line_items":[{"description":"Gear assembly","quantity":5,"unit_price":220.0}]}

## E04.txt
Raw model output:
{"vendor":"Crescent Metals Ltd","invoice_number":"CML-204","date":"2026-01-06","due_date":"2026-01-30","currency":"USD","subtotal":3900.0,"tax":650.0,"total":4550.0,"line_items":[{"description":"Mild steel rods","quantity":130,"unit_price":30.0}]}

## E05.txt
Raw model output:
{"vendor":"Harborline Foods","invoice_number":"HF-991","date":"2026-01-07","due_date":"2026-01-28","currency":"USD","subtotal":560.0,"tax":50.0,"total":610.0,"line_items":[{"description":"Cold-chain carton","quantity":40,"unit_price":14.0}]}

## E06.txt
Raw model output:
{"vendor":"Global Electric Components","invoice_number":"GEC-119","date":"2026-01-07","due_date":"2026-02-05","currency":"USD","subtotal":2400.0,"tax":380.0,"total":2780.0,"line_items":[{"description":"Connector module","quantity":24,"unit_price":100.0}]}

## E07.txt
Raw model output:
{"vendor":"Sterling Petrochem","invoice_number":"STP-51","date":"2026-01-08","due_date":"2026-02-08","currency":"USD","subtotal":1400.0,"tax":175.0,"total":1575.0,"line_items":[{"description":"Industrial solvent drum","quantity":7,"unit_price":200.0}]}

## E08.txt
Raw model output:
{"vendor":"Maple Office Systems","invoice_number":"MOS-3008","date":"2026-01-09","due_date":"2026-02-09","currency":"GBP","subtotal":1120.0,"tax":160.0,"total":1280.0,"line_items":[{"description":"Laser toner pack","quantity":14,"unit_price":80.0}]}

## E09.txt
Raw model output:
{"vendor":"Blue Harbor Logistics","invoice_number":"BHL-72","date":"2026-01-10","due_date":"2026-01-31","currency":"USD","subtotal":1817.27,"tax":181.73,"total":1999.0,"line_items":[{"description":"Customs handling","quantity":1,"unit_price":1817.27}]}

## E10.txt
Raw model output:
{"vendor":"Riverview Packaging","invoice_number":"RVP-22","date":"2026-01-10","due_date":"2026-02-01","currency":"USD","subtotal":700.0,"tax":80.0,"total":780.0,"line_items":[{"description":"Poly bag roll","quantity":20,"unit_price":35.0}]}

## E11.txt
Raw model output:
{"buyer":"Translift Warehousing","supplier":"Arrow Fasteners","po_number":"PO-50112","date":"2026-01-11","delivery_date":null,"currency":"USD","total":2440.0,"items":[{"item_name":"Hex bolt","quantity":4000,"unit_price":0.61}]}

## E12.txt
Raw model output:
{"buyer":"Terra Buildworks","supplier":"Steel Crest","po_number":"PO-77103","date":"2026-01-12","delivery_date":"2026-01-25","currency":"USD","total":6380.0,"items":[{"item_name":"I-beam","quantity":20,"unit_price":319.0}]}

## E13.txt
Raw model output:
{"buyer":"Helios Energy Pvt Ltd","supplier":"Nova Electrics","po_number":"PO-11801","date":"2026-01-13","delivery_date":"2026-02-01","currency":"INR","total":442500.0,"items":[{"item_name":"Control relay","quantity":450,"unit_price":983.0}]}

## E14.txt
Raw model output:
{"buyer":"Westgate Retail Group","supplier":"Urban Shelf Co","po_number":"PO-66290","date":"2026-01-14","delivery":"2026-01-27","currency":"USD","total":3210.0,"items":[{"item_name":"Retail shelf","quantity":30,"unit_price":107.0}]}

## E15.txt
Raw model output:
{"buyer":"Mistral Pharma","supplier":"Northlake Labs","po_number":"PO-22470","date":"2026-01-15","delivery_date":"2026-01-29","currency":"EUR","total":9120.0,"items":[{"item_name":"Sterile vial","quantity":12000,"unit_price":0.76}]}

## E16.txt
Raw model output:
{"buyer":"Artemis Auto Parts","supplier":"Sunline Bearings","po_number":"PO-98340","date":"2026-01-15","delivery_date":null,"currency":"USD","total":2690.0,"items":[{"item_name":"Bearing sleeve","quantity":350,"unit_price":7.69}]}

## E17.txt
Raw model output:
{"buyer":"Summit Textiles","supplier":"Evergreen Dyes","po_number":"PO-40131","date":"2026-01-16","delivery_date":"2026-01-30","currency":"JPY","total":880000.0,"items":[{"item_name":"Reactive dye pack","quantity":220,"unit_price":4000.0}]}

## E18.txt
Raw model output:
{"buyer":"Greenline Agro","supplier":"Orchid Machinery","po_number":"PO-55882","date":"2026-01-17","delivery_date":"2026-02-05","currency":"USD","total":14990.0,"items":[{"item_name":"Seed sorting attachment","quantity":10,"unit_price":1499.0}]}

## E19.txt
Raw model output:
{"buyer":"Pacific Med Devices","supplier":"North Axis Plastics","po_number":"PO-91940","date":"2026-01-18","delivery_date":"2026-02-10","currency":"USD","total":5340.0,"items":[{"item_name":"Medical polymer sheet","quantity":600,"unit_price":8.9}]}

## E20.txt
Raw model output:
{"buyer":"Delta Infrastructure","supplier":"Metro Aggregates","po_number":"PO-70003","date":"2026-01-19","delivery_date":"2026-02-12","currency":"USD","total":26750.0,"items":[{"item_name":"Washed aggregate","quantity":250,"unit_price":107.0}]}
