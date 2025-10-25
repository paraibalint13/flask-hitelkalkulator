# Flask Hitelkalkulátor

Egy egyszerű, magyar nyelvű **Flask webalkalmazás**, amely kiszámolja a havi törlesztőrészletet megadott hitelösszeg, futamidő és kamatláb alapján.  
A projekt célja, hogy bemutassa egy minimális Flask-alkalmazás működését – sablonokkal, űrlapokkal és stílussal.

---

## Funkciók

- Egyszerű, letisztult magyar felhasználói felület  
- Űrlap, amely a hitelösszeget, futamidőt és kamatlábat kéri be  
- Havi törlesztőrészlet kiszámítása annuitás képlettel  
- Szépen formázott, Ft-ban megjelenített eredmény  
- Reszponzív CSS (nincs szükség Bootstrapre)

---

## Képlet

A havi törlesztőrészlet számítása:


T = P \times \frac{r(1+r)^n}{(1+r)^n - 1}


ahol:
- `T` = havi törlesztő (Ft)
- `P` = hitelösszeg (Ft)
- `r` = havi kamatláb (`éves kamat / 12 / 100`)
- `n` = futamidő hónapokban (`év × 12`)

---

