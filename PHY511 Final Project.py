#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

alpha_0 = 1 / 137
mu_ratio = np.logspace(0, 6, 1000)
log_mu_ratio = np.log10(mu_ratio)
alpha_mu = alpha_0 / (1 - (2 * alpha_0 / (3 * np.pi)) * np.log(mu_ratio))
inverse_alpha_mu = 1 / alpha_mu
reference_ratios = np.array([1, 10, 100, 1000, 10000, 1000000])
reference_alpha = alpha_0 / (1 - (2 * alpha_0 / (3 * np.pi)) * np.log(reference_ratios))
reference_inverse = 1 / reference_alpha


# In[8]:


plt.figure(figsize=(10, 6))
plt.plot(
    log_mu_ratio,
    alpha_mu,
    color="blue",
    linewidth=2.5,
    label=r"One-Loop Running Coupling $\alpha(\mu)$"
)
plt.axhline(
    y=alpha_0,
    color="red",
    linestyle="--",
    linewidth=1.8,
    label=r"Reference Coupling $\alpha(\mu_0)=1/137$"
)
plt.scatter(
    np.log10(reference_ratios),
    reference_alpha,
    color="darkblue",
    s=45,
    zorder=5
)
plt.title(
    "Figure 2: One-Loop Evolution of the Fine-Structure Constant",
    fontsize=15
)
plt.xlabel(r"$\ln(\mu/\mu_0)$", fontsize=13)
plt.ylabel(r"Fine-Structure Constant $\alpha(\mu)$", fontsize=13)
plt.xlim(0, 6)
plt.ylim(0.00728, 0.00748)
plt.xticks(np.arange(0, 7, 1))
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()


# In[9]:


plt.figure(figsize=(10, 6))
plt.plot(
    log_mu_ratio,
    inverse_alpha_mu,
    color="darkgreen",
    linewidth=2.5,
    label=r"Inverse Running Coupling $1/\alpha(\mu)$"
)
plt.axhline(
    y=1 / alpha_0,
    color="red",
    linestyle="--",
    linewidth=1.8,
    label=r"Reference Value $1/\alpha(\mu_0)=137$"
)
plt.scatter(
    np.log10(reference_ratios),
    reference_inverse,
    color="green",
    s=45,
    zorder=5
)
plt.title(
    "Figure 3: Inverse Fine-Structure Constant vs. Renormalization Scale",
    fontsize=15
)
plt.xlabel(r"$\ln(\mu/\mu_0)$", fontsize=13)
plt.ylabel(r"Inverse Fine-Structure Constant $1/\alpha(\mu)$", fontsize=13)
plt.xlim(0, 6)
plt.ylim(134, 138)
plt.xticks(np.arange(0, 7, 1))
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()


# In[ ]:




