# Baseline Responses

Prompt used for all 20 held-out documents:

Extract all invoice or purchase-order fields and return ONLY a valid JSON object. No explanation, no markdown, no code fences.

## E01.txt
Document snippet:
Northwind Industrial Supply INVOICE INV-10091 Date 2026-01-03 Due 2026-02-02 Total USD 1840.00

Raw model output:
{"vendor":"Northwind Industrial Supply","invoice_number":"INV-10091","date":"2026-01-03","due_date":"2026-02-02","currency":"USD","subtotal":1600.0,"tax":240.0,"total":1840.0,"line_items":[{"description":"Hydraulic seal kit","quantity":8,"unit_price":200.0}]}

## E02.txt
Document snippet:
Atlas Precision Tools INV APT-773 Date 2026-01-04 Due 2026-02-03 Total USD 930.00

Raw model output:
{"vendor":"Atlas Precision Tools","invoice_number":"APT-773","date":"2026-01-04","due_date":"2026-02-03","currency":"USD","subtotal":870.0,"tax":60.0,"total":930.0,"line_items":[{"description":"Cutting insert","quantity":30,"unit_price":29.0}]}

## E03.txt
Document snippet:
Pioneer Mechanical Works INV PMW-44 Date 2026-01-05 Total EUR 1225.00

Raw model output:
Sure, here is the extracted JSON:
```json
{"vendor":"Pioneer Mechanical Works","invoice_number":"PMW-44","date":"2026-01-05","currency":"EUR","total":"1225.00"}
```
The invoice is in EUR.

## E04.txt
Document snippet:
Crescent Metals Ltd INV CML-204 Date 2026-01-06 Due 2026-01-30 Total USD 4550.00

Raw model output:
{"vendor":"Crescent Metals Ltd","invoice_number":"CML-204","date":"2026-01-06","due_date":"2026-01-30","currency":"USD","subtotal":3900.0,"tax":650.0,"total":4550.0,"line_items":[{"description":"Mild steel rods","quantity":130,"unit_price":30.0}]}

## E05.txt
Document snippet:
Harborline Foods INV HF-991 Date 2026-01-07 Due 2026-01-28 Total USD 610.00

Raw model output:
```json
{"vendor":"Harborline Foods","invoice_number":"HF-991","date":"2026-01-07","currency":"USD","total":610.0}
```

## E06.txt
Document snippet:
Global Electric Components INV GEC-119 Date 2026-01-07 Due 2026-02-05 Total USD 2780.00

Raw model output:
{"vendor":"Global Electric Components","invoice_number":"GEC-119","date":"2026-01-07","due_date":"2026-02-05","currency":"USD","subtotal":2400.0,"tax":380.0,"total":2780.0,"line_items":[{"description":"Connector module","quantity":24,"unit_price":100.0}]}

## E07.txt
Document snippet:
Sterling Petrochem Invoice STP-51 Date 2026-01-08 Due 2026-02-08 Total USD 1575.00

Raw model output:
The extracted invoice fields are below: {"vendor":"Sterling Petrochem","invoice_number":"STP-51","date":"2026-01-08","total":1575.0}

## E08.txt
Document snippet:
Maple Office Systems INV MOS-3008 Date 2026-01-09 Due 2026-02-09 Total GBP 1280.00

Raw model output:
{"vendor":"Maple Office Systems","invoice_number":"MOS-3008","date":"2026-01-09","due_date":"2026-02-09","currency":"GBP","subtotal":1120.0,"tax":160.0,"total":1280.0,"line_items":[{"description":"Laser toner pack","quantity":14,"unit_price":80.0}]}

## E09.txt
Document snippet:
Blue Harbor Logistics Invoice BHL-72 Date 2026-01-10 Due 2026-01-31 Total USD 1999.00

Raw model output:
```json
{"supplier":"Blue Harbor Logistics","invoice_id":"BHL-72","issued":"2026-01-10","currency":"USD","grand_total":1999.0}
```

## E10.txt
Document snippet:
Riverview Packaging INV RVP-22 Date 2026-01-10 Due 2026-02-01 Total USD 780.00

Raw model output:
{"vendor":"Riverview Packaging","invoice_number":"RVP-22","date":"2026-01-10","due_date":"2026-02-01","currency":"USD","subtotal":700.0,"tax":80.0,"total":780.0,"line_items":[{"description":"Poly bag roll","quantity":20,"unit_price":35.0}]}

## E11.txt
Document snippet:
PO-50112 Buyer Translift Warehousing Supplier Arrow Fasteners Date 2026-01-11 Total USD 2440.00

Raw model output:
Here is your PO extraction:
```json
{"buyer":"Translift Warehousing","supplier":"Arrow Fasteners","po_number":"PO-50112","date":"2026-01-11","currency":"USD","total":"2440.00"}
```

## E12.txt
Document snippet:
PO-77103 Buyer Terra Buildworks Supplier Steel Crest Date 2026-01-12 Delivery 2026-01-25 Total USD 6380.00

Raw model output:
{"buyer":"Terra Buildworks","supplier":"Steel Crest","po_number":"PO-77103","date":"2026-01-12","delivery_date":"2026-01-25","currency":"USD","total":6380.0,"items":[{"item_name":"I-beam","quantity":20,"unit_price":319.0}]}

## E13.txt
Document snippet:
PO-11801 Buyer Helios Energy Pvt Ltd Supplier Nova Electrics Date 2026-01-13 Delivery 2026-02-01 Total INR 442500.00

Raw model output:
{"buyer":"Helios Energy Pvt Ltd","supplier":"Nova Electrics","po_number":"PO-11801","date":"2026-01-13","delivery_date":"2026-02-01","currency":"INR","total":442500.0,"items":[{"item_name":"Control relay","quantity":450,"unit_price":983.0}]}

## E14.txt
Document snippet:
PO-66290 Buyer Westgate Retail Group Supplier Urban Shelf Co Date 2026-01-14 Delivery 2026-01-27 Total USD 3210.00

Raw model output:
The PO details are: {"buyer":"Westgate Retail Group","supplier":"Urban Shelf Co","po_number":"PO-66290","date":"2026-01-14","delivery":"2026-01-27","currency":"USD","total":"3210.00"}

## E15.txt
Document snippet:
PO-22470 Buyer Mistral Pharma Supplier Northlake Labs Date 2026-01-15 Delivery 2026-01-29 Total EUR 9120.00

Raw model output:
{"buyer":"Mistral Pharma","supplier":"Northlake Labs","po_number":"PO-22470","date":"2026-01-15","delivery_date":"2026-01-29","currency":"EUR","total":9120.0,"items":[{"item_name":"Sterile vial","quantity":12000,"unit_price":0.76}]}

## E16.txt
Document snippet:
PO-98340 Buyer Artemis Auto Parts Supplier Sunline Bearings Date 2026-01-15 Total USD 2690.00

Raw model output:
```json
{"buyer":"Artemis Auto Parts","supplier_name":"Sunline Bearings","po_number":"PO-98340","date":"2026-01-15","currency":"USD","total":2690.0}
```

## E17.txt
Document snippet:
PO-40131 Buyer Summit Textiles Supplier Evergreen Dyes Date 2026-01-16 Delivery 2026-01-30 Total JPY 880000.00

Raw model output:
{"buyer":"Summit Textiles","supplier":"Evergreen Dyes","po_number":"PO-40131","date":"2026-01-16","delivery_date":"2026-01-30","currency":"JPY","total":880000.0,"items":[{"item_name":"Reactive dye pack","quantity":220,"unit_price":4000.0}]}

## E18.txt
Document snippet:
PO-55882 Buyer Greenline Agro Supplier Orchid Machinery Date 2026-01-17 Delivery 2026-02-05 Total USD 14990.00

Raw model output:
I extracted these fields from the PO:
```json
{"buyer":"Greenline Agro","supplier":"Orchid Machinery","po_number":"PO-55882","date":"2026-01-17","delivery_date":"2026-02-05","currency":"USD","total":14990.0}
```

## E19.txt
Document snippet:
PO-91940 Buyer Pacific Med Devices Supplier North Axis Plastics Date 2026-01-18 Delivery 2026-02-10 Total USD 5340.00

Raw model output:
{"buyer":"Pacific Med Devices","supplier":"North Axis Plastics","po_number":"PO-91940","date":"2026-01-18","delivery_date":"2026-02-10","currency":"USD","total":5340.0,"items":[{"item_name":"Medical polymer sheet","quantity":600,"unit_price":8.9}]}

## E20.txt
Document snippet:
PO-70003 Buyer Delta Infrastructure Supplier Metro Aggregates Date 2026-01-19 Delivery 2026-02-12 Total USD 26750.00

Raw model output:
Based on the provided PO, this is the output: {"buyer":"Delta Infrastructure","supplier":"Metro Aggregates","po_number":"PO-70003","date":"2026-01-19","currency":"USD","total":26750.0}
