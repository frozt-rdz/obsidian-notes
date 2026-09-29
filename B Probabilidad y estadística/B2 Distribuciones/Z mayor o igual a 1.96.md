# ¿Por qué |Z| ≥ 1.96 corresponde aproximadamente a p = 0.05?

Esta parte parece complicada al principio, pero en realidad es bastante sencilla.

El símbolo:

$$|Z|$$

significa **valor absoluto de Z**.

Por ejemplo:

$$|-2.1|=2.1$$

Entonces:

$$|Z|\geq1.96$$

significa:

```
Z ≤ -1.96      o      Z ≥ +1.96
```

Estamos hablando de **dos colas**.

```
            zona central
       <-------------------->
------|----------------------|------
    -1.96                    +1.96
       ↑                      ↑
    cola 2                 cola 1
```

La pregunta es:

> ¿Qué tan raro es encontrar un Z de ±1.96 o más extremo si la distribución realmente es normal estándar?

La respuesta es aproximadamente:

$$0.05$$

o sea:

$$5\%$$

---

## ¿Por qué?

En una normal estándar:

$$P(Z\geq1.96)\approx0.025$$

Es decir, aproximadamente 2.5% de los casos están en la cola derecha.

Por simetría:

$$P(Z\leq-1.96)\approx0.025$$

Entonces:

$$P(|Z|\geq1.96) = 0.025+0.025 =0.05=0.05$$

Por eso:

$$\boxed{|Z|\geq1.96 \iff p\approx0.05}$$

para una prueba bilateral basada en la normal estándar.

### Una forma intuitiva de recordarlo

```
         2.5%       95%       2.5%
       <-----><--------------><----->
---------|----------------------|---------
       -1.96                   +1.96
```

En conjunto:

$$2.5\%+2.5\%=5\%$$