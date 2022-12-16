# Policy Gradient Algorithms for Invalid Action Masking

This repo is inherited from the paper A Closer Look at Invalid Action Masking in Policy Gradient Algorithms [paper](https://arxiv.org/abs/2006.14171) [code](https://github.com/vwxyzjn/invalid-action-masking). In this repo, we provide the source code to reproduce the results in the paper (Policy Gradient Algorithms for Invalid Action Masking). 

## Get started

Please refer to this [repo](https://github.com/vwxyzjn/invalid-action-maskin).

## Algorithms

Here is a description of related algorithms in this repo:
* `algos/On-PIAM_NxN.py`: This is a pytorch implementation of On-PIAM for $N$x$N$ map.
* `algos/Off-PIAM_NxN.py`: This is a pytorch implementation of Off-PIAM for $N$x$N$ map.
* `algos/CO-IAM_NxN.py`: This is a pytorch implementation of CO-IAM for $N$x$N$ map.
* `algos/Penalty_NxN.py`: This is a pytorch implementation of invalid action penalty for $N$x$N$ map.

## Reproduce All of Our Experiments

To reproduce all of our experiments, try running:

```
cd script
bash script0.sh
bash script1.sh
bash script2.sh
bash script3.sh
bash script4.sh
```

## Reproduce The Figures and Tables

To reproduce the figures and tables, try running:

```
cd plots
python episode_reward.py
python eval_episode_reward.py
python approx_kl.py
python analysis.py
```

