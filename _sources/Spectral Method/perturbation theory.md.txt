# l2 Perturbation Theory
## Lemma 

The following identities are true:
$$
\begin{gathered}
\left\|\boldsymbol{U} \boldsymbol{U}^{\top}-\boldsymbol{U}^{\star} \boldsymbol{U}^{\star \top}\right\|=\|\sin \boldsymbol{\Theta}\|=\left\|\boldsymbol{U}_{\perp}^{\top} \boldsymbol{U}^{\star}\right\|=\left\|\boldsymbol{U}^{\top} \boldsymbol{U}_{\perp}^{\star}\right\| \\
\frac{1}{\sqrt{2}}\left\|\boldsymbol{U} \boldsymbol{U}^{\top}-\boldsymbol{U}^{\star} \boldsymbol{U}^{\star \top}\right\|_{\mathrm{F}}=\|\sin \boldsymbol{\Theta}\|_{\mathrm{F}}=\left\|\boldsymbol{U}_{\perp}^{\top} \boldsymbol{U}^{\star}\right\|_{\mathrm{F}}=\left\|\boldsymbol{U}^{\top} \boldsymbol{U}_{\perp}^{\star}\right\|_{\mathrm{F}}
\end{gathered}
$$
$$
\begin{gathered}
\left\|\boldsymbol{U} \boldsymbol{U}^{\top}-\boldsymbol{U}^{\star} \boldsymbol{U}^{\star \top}\right\| \leq \min _{\boldsymbol{m} \in \mathcal{O}^{r \times r}}\left\|\boldsymbol{U} \boldsymbol{R}-\boldsymbol{U}^{\star}\right\| \leq \sqrt{2}\left\|\boldsymbol{U} \boldsymbol{U}^{\top}-\boldsymbol{U}^{\star} \boldsymbol{U}^{\star T}\right\| ; \\
\frac{1}{\sqrt{2}}\left\|\boldsymbol{U} \boldsymbol{U}^{\top}-\boldsymbol{U}^{\star} \boldsymbol{U}^{\star \top}\right\|_{\mathrm{F}} \leq \min _{\boldsymbol{R} \in \mathcal{O}^{\star} \times \boldsymbol{r}}\left\|\boldsymbol{U} \boldsymbol{R}-\boldsymbol{U}^{\star}\right\|_{\mathrm{F}} \leq\left\|\boldsymbol{U} \boldsymbol{U}^{\top}-\boldsymbol{U}^{\star} \boldsymbol{U}^{\star \top}\right\|_{\mathrm{F}} .
\end{gathered}
$$
## Theorems
We use the Distance modulo optimal rotation
$$
\begin{aligned}
\operatorname{dist}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right) &:=\min _{\boldsymbol{R} \in \mathcal{O}^{r} \times r}\left\|\boldsymbol{U} \boldsymbol{R}-\boldsymbol{U}^{\star}\right\| \\
\operatorname{dist}_{\mathrm{F}}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right) &:=\min _{\boldsymbol{R} \in \mathcal{O}^{r \times r}}\left\|\boldsymbol{U} \boldsymbol{R}-\boldsymbol{U}^{\star}\right\|_{\mathrm{F}}
\end{aligned}
$$

```{admonition} Davis-Kahan’s $sin \boldsymbol{\Theta}$ theorem(simple version).
:class: note


Suppose $\boldsymbol{M}^{\star} \succeq \mathbf{0}$ and is rank-r. If $\|\boldsymbol{E}\|<(1-1 / \sqrt{2}) \lambda_{r}\left(\boldsymbol{M}^{\star}\right)$, then
$$
\begin{gathered}
\operatorname{dist}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right) \leq \sqrt{2}\|\sin \boldsymbol{\Theta}\| \leq \frac{2\left\|\boldsymbol{E} \boldsymbol{U}^{\star}\right\|}{\lambda_{r}\left(\boldsymbol{M}^{\star}\right)} \leq \frac{2\|\boldsymbol{E}\|}{\lambda_{r}\left(\boldsymbol{M}^{\star}\right)} \\
\operatorname{dist}_{F}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right) \leq \sqrt{2}\|\sin \boldsymbol{\Theta}\|_{\mathrm{F}} \leq \frac{2\left\|\boldsymbol{E} \boldsymbol{U}^{\star}\right\|_{\mathrm{F}}}{\lambda_{r}\left(\boldsymbol{M}^{\star}\right)} \leq \frac{2 \sqrt{r}\|\boldsymbol{E}\|}{\lambda_{r}\left(\boldsymbol{M}^{\star}\right)}
\end{gathered}
$$
```

### Davis-Kahan’s $sin \boldsymbol{\Theta}$ theorem(General version)

Assume that
$$
\begin{aligned}
&\text { eigenvalues }\left(\boldsymbol{\Lambda}^{\star}\right) \subseteq(-\infty, \alpha-\Delta] \cup[\beta+\Delta, \infty) \\
&\operatorname{eigenvalues}\left(\boldsymbol{\Lambda}_{\perp}\right) \subseteq[\alpha, \beta]
\end{aligned}
$$
for some quantities $\alpha, \beta \in \mathbb{R}$ and eigengap $\Delta>0$. Then one has
$$
\begin{gathered}
\operatorname{dist}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right) \leq \sqrt{2}\|\sin \boldsymbol{\Theta}\| \leq \frac{\sqrt{2}\left\|\boldsymbol{E} \boldsymbol{U}^{\star}\right\|}{\Delta} \leq \frac{\sqrt{2}\|\boldsymbol{E}\|}{\Delta} \\
\operatorname{dist}_{\mathrm{F}}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right) \leq \sqrt{2}\|\sin \boldsymbol{\Theta}\|_{\mathrm{F}} \leq \frac{\sqrt{2}\left\|\boldsymbol{E} \boldsymbol{U}^{\star}\right\|_{\mathrm{F}}}{\Delta} \leq \frac{\sqrt{2 r}\|\boldsymbol{E}\|}{\Delta}
\end{gathered}
$$

### Wedin’s sinΘ theorem
If $\|\boldsymbol{E}\|<\sigma_{r}^{\star}-\sigma_{r+1}^{\star}$, then one has
$$
\begin{gathered}
\max \left\{\operatorname{dist}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right), \operatorname{dist}\left(\boldsymbol{V}, \boldsymbol{V}^{\star}\right)\right\} \leq \frac{\sqrt{2} \max \left\{\left\|\boldsymbol{E}^{\top} \boldsymbol{U}^{\star}\right\|,\left\|\boldsymbol{E} \boldsymbol{V}^{\star}\right\|\right\}}{\sigma_{r}^{\star}-\sigma_{r+1}^{\star}-\|\boldsymbol{E}\|} \\
\max \left\{\operatorname{dist}_{\mathrm{F}}\left(\boldsymbol{U}, \boldsymbol{U}^{\star}\right), \operatorname{dist}_{\mathrm{F}}\left(\boldsymbol{V}, \boldsymbol{V}^{\star}\right)\right\} \leq \frac{\sqrt{2} \max \left\{\left\|\boldsymbol{E}^{\top} \boldsymbol{U}^{\star}\right\|_{\mathrm{F}},\left\|\boldsymbol{E} \boldsymbol{V}^{\star}\right\|_{\mathrm{F}}\right\}}{\sigma_{r}^{\star}-\sigma_{r+1}^{\star}-\|\boldsymbol{E}\|}
\end{gathered}
$$