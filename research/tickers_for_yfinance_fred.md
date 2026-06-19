Acá tenés la tabla actualizada con todas las columnas integradas.

Para que los datos tengan sentido al cruzarlos, tené en cuenta que **FRED y Yahoo Finance miden cosas conceptualmente distintas**: FRED registra precios físicos de la economía real o índices gubernamentales, mientras que `yfinance` extrae datos de la bolsa de valores (por eso los tickers agregados corresponden a contratos de **Futuros**).

### Tabla de Commodities, FRED y YFinance

| Commodity | FRED Series ID | Ticker `yfinance` | Source ID | Release ID | Descripción en FRED | Frecuencia |
| --- | --- | --- | --- | --- | --- | --- |
| **Crude Oil (Petróleo)** | `DCOILWTICO` | `CL=F` | 53 | *Ver nota* | Precio Spot del WTI (Cushing, Oklahoma). Es el benchmark de EE.UU. | Diaria |
| **Copper (Cobre)** | `PCOPPUSDM` | `HG=F` | 60 | 365 | Precio global del cobre por tonelada métrica (Datos del FMI). | Mensual |
| **Aluminum (Aluminio)** | `PALUMUSDM` | `ALI=F` | 60 | 365 | Precio global del aluminio por tonelada métrica (Datos del FMI). | Mensual |
| **Iron Ore (Hierro)** | `PIORECRUSDM` | `TIO=F` | 60 | 365 | Precio global del mineral de hierro por tonelada métrica. | Mensual |
| **Zinc** | `PZINCUSDM` | `ZNC=F` | 60 | 365 | Precio global del zinc por tonelada métrica (Datos del FMI). | Mensual |
| **Lumber (Madera)** | `WPU0811` | `LBS=F` | 22 | 46 | Índice de Precios al Productor (PPI) de madera blanda. EE.UU. | Mensual |
| **Steel (Acero)** | `WPS101` | `HRC=F` | 22 | 46 | Índice de Precios al Productor (PPI) de Hierro y Acero. | Mensual |

---

### Detalles de los IDs de FRED agregados

**Acerca de los Source IDs (Quién genera el dato):**

* **53:** U.S. Energy Information Administration (EIA).
* **60:** International Monetary Fund (Fondo Monetario Internacional).
* **22:** U.S. Bureau of Labor Statistics (BLS).

**Acerca de los Release IDs (El evento de publicación):**

* **365:** Es el código del reporte *"Primary Commodity Prices"* que el FMI libera cada mes. Agrupa a todos los metales de la tabla.
* **46:** Es el código general del *"Producer Price Index"* (Índice de Precios al Productor) de Estados Unidos.
* ***Nota sobre el Petróleo:** La EIA clasifica el petróleo bajo su publicación de *"Spot Prices"*, pero a diferencia de los grandes reportes mensuales (como el 46 o el 365), la asignación de su Release ID interno suele ser dinámica o menos estructurada en la documentación de la API. Si en tu programa estrictamente necesitás guardar ese ID, la mejor práctica es consultarlo dinámicamente haciendo un llamado al endpoint `fred/series/release?series_id=DCOILWTICO`.

### Aclaración técnica sobre los tickers de YFinance

Como los commodities no son acciones de empresas, en Yahoo Finance no vas a encontrar el "spot price" puro. Los tickers listados (que terminan en `=F`) corresponden a los contratos de mercado a futuro más líquidos para ese material:

* `CL=F`: Crude Oil Futures
* `HG=F`: Copper Futures
* `ALI=F`: Aluminum Futures
* `TIO=F`: Iron Ore Futures
* `ZNC=F`: Zinc Futures
* `LBS=F`: Random Length Lumber Futures
* `HRC=F`: US Midwest Domestic Hot-Rolled Coil Steel Futures