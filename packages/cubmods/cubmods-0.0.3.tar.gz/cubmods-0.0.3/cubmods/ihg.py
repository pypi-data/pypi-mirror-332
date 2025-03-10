# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long, invalid-name, too-many-arguments, too-many-locals, too-many-statements, trailing-whitespace
r"""
.. _ihg0-module:

CUB models in Python.
Module for IHG (Inverse HyperGeometric).

Description:
============
    This module contains methods and classes
    for IHG model family without covariates.

Manual, Examples and References:
================================
    - `Models manual <manual.html#ihg-without-covariates>`__
  
List of TODOs:
==============
  - ...

Credits
==============
    :Author:      Massimo Pierini
    :Date:        2023-24
    :Credits:     Domenico Piccolo, Rosaria Simone
    :Contacts:    cub@maxpierini.it

Classes and Functions
=====================
"""

import datetime as dt
import numpy as np
import scipy.stats as sps
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from statsmodels.tools.numdiff import approx_hess
#import matplotlib.pyplot as plt
from .general import (
    choices, freq, aic, bic,
    luni, lsat, dissimilarity
)
from .smry import CUBres, CUBsample

def pmf(m, theta):
    r"""Probability distribution of a specified IHG model without covariates.

    :math:`\Pr(R = r | \pmb\theta),\; r=1 \ldots m`

    :param m: number of ordinal categories
    :type m: int
    :param theta: parameter :math:`\theta` (probability of 1st shelter category)
    :type theta: float
    :return: the vector of the probability distribution of a CUB model.
    :rtype: numpy array
    """
    pr = np.repeat(np.nan, m)
    pr[0] = theta
    for i in range(m-1):
        j = i + 1
        pr[j] = pr[i]*(1-theta)*(m-j)/(m-j-1+j*theta)
    return pr

def loglik(m, theta, f):
    """
    Compute the log-likelihood function of a IHG model without 
    covariates for a given absolute frequency distribution.

    :param theta: parameter :math:`\theta` (probability of 1st shelter category)
    :type theta: float
    :param m: number of ordinal categories
    :type m: int
    :param f: array of absolute frequency distribution
    :type f: array of int
    :return: the log-likelihood value
    :rtype: float
    """
    p = pmf(m=m, theta=theta)
    l = (f*np.log(p)).sum()
    return l

def effe(theta, m, f):
    r"""Compute the negative log-likelihood function of a IHG model without 
    covariates for a given absolute frequency distribution.
    Auxiliary function of ``mle()`` for optimization algorithm.

    :param theta: parameter :math:`\theta` (probability of 1st shelter category)
    :type theta: float
    :param m: number of ordinal categories
    :type m: int
    :param f: array of absolute frequency distribution
    :type f: array of int
    :return: the log-likelihood value
    :rtype: float
    """
    return -loglik(m=m, theta=theta, f=f)

def init_theta(m, f):
    r"""Preliminary estimators for IHG models without covariates.

    Computes preliminary parameter estimates of a IHG model without covariates for given ordinal
    responses. These preliminary estimators are used within the package code to start the E-M algorithm.

    :param f: array of the absolute frequencies of given ordinal responses
    :type f: array of int
    :param m: number of ordinal categories
    :type m: int
    :return: the value of :math:`\theta^{(0)}`
    """
    R = choices(m)
    aver = (R*f).sum()/f.sum()
    est = (m-aver)/(1+(m-2)*aver)
    return est

def draw(m, theta, n,
    df, formula, seed=None):
    r"""Draw a random sample from a specified IHG model.

    :param m: number of ordinal categories
    :type m: int
    :param theta: parameter :math:`\theta` (probability of 1st shelter category)
    :type theta: float
    :param n: number of ordinal responses to be drawn
    :type n: int
    :param df: original DataFrame
    :type df: DataFrame
    :param formula: the formula used
    :type formula: str
    :param seed: the `seed` to ensure reproducibility, defaults to None
    :type seed: int, optional
    :return: an instance of ``CUBsample`` (see `here <cubmods.html#cubmods.smry.CUBsample>`__) containing ordinal responses drawn from the specified model
    """
    theoric = pmf(m=m, theta=theta)
    np.random.seed(seed)
    rv = np.random.choice(
        choices(m=m),
        size=n,
        replace=True,
        p=theoric
    )
    f = freq(m=m, sample=rv)
    diss = dissimilarity(f/n, theoric)
    pars = np.array([theta])
    par_names = np.array(["theta"])
    p_types = np.array(["Theta"])
    sample = CUBsample(
        model="IHG",
        rv=rv, m=m,
        pars=pars,
        par_names=par_names,
        p_types=p_types,
        seed=seed, theoric=theoric,
        diss=diss, df=df,
        formula=formula
    )
    return sample

def var(m, theta):
    r"""Variance of a specified IHG model.

    :param m: number of ordinal categories
    :type m: int
    :param theta: parameter :math:`\theta` (probability of 1st shelter category)
    :type theta: float
    :return: the variance of the model
    :rtype: float
    """
    n = theta*(1-theta)*(m-theta)*(m-1)**2
    d1 = (theta*(m-2)+1)**2
    d2 = (theta*(m-3)+2)
    return n/(d1*d2)

def mle(m, sample, 
    df, formula, ass_pars=None):
    r"""Main function for CUB models without covariates.

    Function to estimate and validate a CUB model without covariates for given ordinal responses.

    :param sample: array of ordinal responses
    :type sample: array of int
    :param m: number of ordinal categories
    :type m: int
    :param df: original DataFrame
    :type df: DataFrame
    :param formula: the formula used
    :type formula: str
    :param ass_pars: dictionary of hypothesized parameters, defaults to None
    :type ass_pars: dictionary, optional
    :return: an instance of ``CUBresIHG`` (see the Class for details)
    :rtype: object
    """
    start = dt.datetime.now()
    f = freq(sample=sample, m=m)
    n = sample.size
    theta0 = init_theta(m, f)
    opt = minimize(
        effe, x0=theta0,
        #bracket=(0, 1),
        bounds=[(1e-16, 1-1e-16)],
        args=(m, f),
        method="L-BFGS-B",
    )
    theta = opt.x
    infmat = approx_hess([theta0], effe,
        args=(m, f))
    #varmat = np.ndarray(shape=(opt.size,opt.size))
    varmat = np.nan
    if np.any(np.isnan(infmat)):
        print("WARNING: NAs produced in information matrix")
    elif np.linalg.det(infmat) <= 0:
        print("ATTENTION: information matrix NOT positive definite")
    else:
        # varmat = np.linalg.inv(infmat)/n
        varmat = np.linalg.inv(infmat)
    end = dt.datetime.now()
    stderrs = np.sqrt(np.diag(varmat))
    wald = theta/stderrs
    pval = 2*(sps.norm().sf(abs(wald)))
    #print(theta, stderrs, wald, pval)
    l = loglik(m=m, theta=theta, f=f)
    muloglik = l/n
    AIC = aic(l=l, p=1)
    BIC = bic(l=l, p=1, n=n)
    loglikuni = luni(m=m, n=n)
    logliksat = lsat(n=n, f=f)
    dev = 2*(logliksat-l)
    theoric = pmf(m=m, theta=theta)
    diss = dissimilarity(f/n, theoric)
    #end = dt.datetime.now()
    
    #print(f"theta={theta}")
    #print(f"SE={stderrs}")
    
    return CUBresIHG(
        model="IHG",
        m=m, n=n,
        theoric=theoric,
        e_types=["Theta"],
        est_names=["theta"],
        estimates=theta,
        stderrs=stderrs, pval=pval,
        wald=wald, loglike=l,
        muloglik=muloglik,
        logliksat=logliksat,
        loglikuni=loglikuni,
        dev=dev, AIC=AIC, BIC=BIC,
        diss=diss, sample=sample,
        f=f, varmat=varmat,
        seconds=(end-start).total_seconds(),
        time_exe=start, ass_pars=ass_pars,
        df=df, formula=formula
    )

class CUBresIHG(CUBres):
    r"""Object returned by ``.mle()`` function.
    See `here <cubmods.html#cubmods.smry.CUBres>`__ the Base for details.
    """
    def plot_estim(self, ci=.95, ax=None,
        magnified=False):
        r"""Plots the estimated parameter values in the parameter space and
        the asymptotic standard error.
        
        :param figsize: tuple of ``(length, height)`` for the figure (useful only if ``ax`` is not None)
        :type figsize: tuple of float
        :param ci: level :math:`(1-\alpha/2)` for the confidence ellipse
        :type ci: float
        :param magnified: if False the limits will be the entire parameter space, otherwise let matplotlib choose the limits
        :type magnified: bool
        :param ax: matplotlib axis, if None a new figure will be created, defaults to None
        :type ax: matplolib ax, optional
        :return: ``ax`` or a tuple ``(fig, ax)``
        """
        theta = self.estimates
        se = self.stderrs
        # change all spines
        for axis in ['bottom']:
            ax.spines[axis].set_linewidth(2)
            # increase tick width
            ax.tick_params(width=2)
        ax.axhline(0, color="orange")
        ax.set_ylim((-.1, +.1))
        ax.plot(theta, 0, ".b",
            ms=20, alpha=.5,
            label="estimated")
        if ci is not None:
            alpha = 1-ci
            z = abs(sps.norm().ppf(alpha/2))
            ax.errorbar(
                theta, 0,
                xerr=z*self.stderrs,
                ecolor="b",
                elinewidth=2,
                capsize=5,
                label=f"{ci:.0%} CI"
            )
        if self.ass_pars is not None:
            ax.scatter(self.ass_pars['theta'], 0,
                facecolor="None",
                edgecolor="r", s=200, label="assumed")
        ax.legend(loc="upper left",
            bbox_to_anchor=(1,1))
        ax.set_yticks([])
        ax.grid(True)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        #ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.subplots_adjust(
            hspace = 0.3
        )
        if not magnified:
            ax.set_xlim([0,1])
            ax.set_xticks(np.arange(
                0,10.1)/10)
        ax.set_xlabel(r"$\theta$ parameter")
    
    def plot_ordinal(self,
        figsize=(7, 5),
        ax=None, kind="bar",
        saveas=None
        ):
        r"""Plots relative frequencies of observed sample, estimated probability distribution and,
        if provided, probability distribution of a known model.

        :param figsize: tuple of ``(length, height)`` for the figure (useful only if ``ax`` is not None)
        :type figsize: tuple of float
        :param kind: choose a barplot (``'bar'`` default) of a scatterplot (``'scatter'``)
        :type kind: str
        :param ax: matplotlib axis, if None a new figure will be created, defaults to None
        :type ax: matplolib ax, optional
        :param saveas: if provided, name of the file to save the plot
        :type saveas: str
        :return: ``ax`` or a tuple ``(fig, ax)``
        """
        if ax is None:
            fig, ax = plt.subplots(
                figsize=figsize
            )
        else:
            fig = None
        
        title = f"{self.model} model    "
        title += f"$n={self.n}$\n"
        title += fr"Estim($\theta={self.estimates[0]:.3f}$)"
        title += f"    Dissim(est,obs)={self.diss:.4f}"
        if self.ass_pars is not None:
            title += "\n"
            title += fr"Assumed($\theta={self.ass_pars['theta']:.3f}$)"
            p_gen = pmf(m=self.m, theta=self.ass_pars['theta'])
            R = choices(m=self.m)
            ax.stem(R, p_gen, linefmt="--r",
                markerfmt="none", label="assumed")
        ax.set_title(title)

        R = choices(self.m)
        ax.set_xticks(R)
        ax.set_xlabel("Ordinal")
        ax.set_ylabel("Probability")

        ax.plot(R, self.theoric, ".b:",
            label="estimated", ms=10)
        if kind == "bar":
            ax.bar(R, self.f/self.n,
                facecolor="None",
                edgecolor="k",
                label="observed")
        else:
            if kind != "scatter":
                print(f"WARNING: kind `{kind}` unknown. Using `scatter` instead.")
            ax.scatter(R, self.f/self.n,
                facecolor="None",
                edgecolor="k", s=200,
                label="observed")

        ax.set_ylim((0, ax.get_ylim()[1]))
        ax.legend(loc="upper left",
            bbox_to_anchor=(1,1))

        if fig is not None:
            if saveas is not None:
                fig.savefig(saveas, bbox_inches='tight')
        return fig, ax

    def plot(self,
        ci=.95,
        saveas=None,
        figsize=(7, 8)
        ):
        r"""Main function to plot an object of the Class.

        :param figsize: tuple of ``(length, height)`` for the figure
        :type figsize: tuple of float
        :param ci: level :math:`(1-\alpha/2)` for the standard error
        :type ci: float
        :param saveas: if provided, name of the file to save the plot
        :type saveas: str
        :return: ``ax`` or a tuple ``(fig, ax)``
        """
        fig, ax = plt.subplots(3, 1, figsize=figsize,
                               height_ratios=[.8, .1, .1])
        self.plot_ordinal(ax=ax[0])
        self.plot_estim(ax=ax[1], ci=ci)
        self.plot_estim(ax=ax[2], ci=ci,
            magnified=True)
        if saveas is not None:
            fig.savefig(saveas, bbox_inches='tight')
        return fig, ax
