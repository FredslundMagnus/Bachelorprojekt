
# Parameters

    Name :                      Diamonds2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      54180968045 function calls (52504766188 primitive calls) in 258900.49 seconds

##    Ordered by: cumulative time
   List reduced from 426 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.494 258900.494 {built-in method builtins.exec}
                      1    0.375    0.375 258900.494 258900.494 <string>:1(<module>)
                      1 6090.293 6090.293 258900.118 258900.118 optionCritic.py:195(option_critic_run)
               59608875 9551.887    0.000 112796.963    0.002 optionCritic.py:143(actor_loss_fn)
        2215388134/546935734 10399.500    0.000 111938.039    0.000 module.py:866(_call_impl)
              185383600  876.943    0.000 104050.251    0.001 optionCritic.py:70(get_state)
              185383600 2338.300    0.000 100601.467    0.001 container.py:117(forward)
                2384355   19.226    0.000 74342.947    0.031 tensor.py:195(backward)
                2384355   24.838    0.000 74323.403    0.031 __init__.py:68(backward)
                2384355 74242.139    0.031 74242.139    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              370767200  973.514    0.000 63096.618    0.000 conv.py:398(forward)
              370767200  529.233    0.000 61729.905    0.000 conv.py:390(_conv_forward)
              370767200 61200.672    0.000 61200.672    0.000 {built-in method conv2d}
               59608875 3606.764    0.000 21198.117    0.000 optionCritic.py:91(get_action)
              732319334 1688.025    0.000 21119.621    0.000 linear.py:93(forward)
              732319334  694.261    0.000 18734.028    0.000 functional.py:1737(linear)
              732319334 17881.704    0.000 17881.704    0.000 {built-in method torch._C._nn.linear}
               59608875 1247.248    0.000 14368.101    0.000 optionCritic.py:80(predict_option_termination)
              119217750 1225.134    0.000 8142.154    0.000 distribution.py:34(__init__)
              556150800  533.894    0.000 7607.734    0.000 activation.py:713(forward)
              556150800  570.043    0.000 7073.840    0.000 functional.py:1364(leaky_relu)
               59608875  614.753    0.000 7044.228    0.000 categorical.py:115(log_prob)
                2384355   54.927    0.000 6857.001    0.003 optimizer.py:84(wrapper)
                2384355   31.001    0.000 6663.602    0.003 grad_mode.py:24(decorate_context)
                2384355  138.450    0.000 6580.228    0.003 rmsprop.py:56(step)
              556150800 6393.801    0.000 6393.801    0.000 {built-in method torch._C._nn.leaky_relu}
                2384355  135.454    0.000 6291.353    0.003 _functional.py:203(rmsprop)
               59608875  805.789    0.000 5964.594    0.000 categorical.py:49(__init__)
              182129421  405.522    0.000 5854.091    0.000 optionCritic.py:77(get_Q)
               59608875  468.996    0.000 5568.136    0.000 bernoulli.py:34(__init__)
                 596088   97.629    0.000 4860.072    0.008 optionCritic.py:116(critic_loss_fn)
              119813838  420.846    0.000 4515.967    0.000 optionCritic.py:88(get_terminations)
                2384355   12.527    0.000 4414.966    0.002 game.py:41(step)
                2384355   22.188    0.000 4272.667    0.002 layers.py:718(step)
               59608875 2457.355    0.000 3633.230    0.000 constraints.py:398(check)
               59608875  499.310    0.000 2859.324    0.000 distribution.py:240(_validate_sample)
               33380964 2830.142    0.000 2830.142    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2384356  196.493    0.000 2264.200    0.001 layers.py:684(update)
              185383600  232.248    0.000 2141.819    0.000 activation.py:101(forward)
               59608875 2083.865    0.000 2083.865    0.000 constraints.py:364(check)
               59608875  445.277    0.000 2047.430    0.000 bernoulli.py:86(sample)
               33380964 2036.713    0.000 2036.713    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2384355   86.234    0.000 1977.999    0.001 layers.py:17(step)
               59608875 1020.007    0.000 1941.670    0.000 categorical.py:123(entropy)
              185383600  204.576    0.000 1909.571    0.000 functional.py:1195(relu)
               59608875  147.149    0.000 1882.800    0.000 layer.py:98(move)
             2872636571 1862.625    0.000 1862.797    0.000 module.py:934(__getattr__)
               59608875 1852.618    0.000 1852.618    0.000 constraints.py:249(check)
              178826625  242.642    0.000 1756.185    0.000 utils.py:106(__get__)
              185383600  171.276    0.000 1687.159    0.000 flatten.py:39(forward)
              417262125 1685.459    0.000 1685.459    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              185383600 1675.114    0.000 1675.114    0.000 {built-in method relu}
              180018801  191.133    0.000 1606.442    0.000 tensor.py:525(__rsub__)
              185383600 1515.883    0.000 1515.883    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 596088 1269.242    0.002 1507.512    0.003 replaybuffer.py:42(sample_option_critic)
              119217750  519.593    0.000 1481.942    0.000 functional.py:46(broadcast_tensors)
               26227905   61.672    0.000 1446.268    0.000 tensor.py:575(__iter__)
               59608875  383.186    0.000 1387.832    0.000 categorical.py:108(sample)
              180018801 1385.198    0.000 1385.198    0.000 {built-in method rsub}
               26227905 1347.828    0.000 1347.828    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               59608875   71.531    0.000 1326.323    0.000 categorical.py:88(logits)
             2241616039 1313.937    0.000 1313.937    0.000 {built-in method torch._C._get_tracing_state}
              119813838 1276.561    0.000 1276.561    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              179422713 1274.349    0.000 1274.349    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               59608875   73.275    0.000 1254.792    0.000 utils.py:82(probs_to_logits)
               59608875  271.480    0.000 1229.904    0.000 utils.py:11(broadcast_all)
              178826625 1209.582    0.000 1209.582    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9587414759 1165.413    0.000 1182.025    0.000 {built-in method builtins.len}
               59608875  253.980    0.000 1160.916    0.000 layers.py:735(check)
                2110647   30.515    0.000 1041.763    0.000 layers.py:740(restart)
              178826625 1020.128    0.000 1020.128    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9046936136  960.493    0.000  960.493    0.000 {method 'values' of 'collections.OrderedDict' objects}
               59608875  913.596    0.000  913.596    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2110647   17.197    0.000  822.211    0.000 level.py:8(__init__)
              119217750  807.971    0.000  807.971    0.000 {built-in method broadcast_tensors}
                2384355   87.263    0.000  767.989    0.000 replaybuffer.py:34(save_option_critic)
                2384355  108.550    0.000  761.340    0.000 optimizer.py:189(zero_grad)
               59608875  152.674    0.000  733.253    0.000 utils.py:77(clamp_probs)
                2110647   34.944    0.000  705.797    0.000 levels.py:151(generate)
              180614889  642.625    0.000  642.625    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               10129026  119.183    0.000  635.797    0.000 level.py:41(notUsed)
               61719495  613.471    0.000  613.471    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               59608875  611.740    0.000  611.740    0.000 {built-in method bernoulli}
               59608875  590.676    0.000  590.676    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               12848975  277.565    0.000  588.691    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               59608875  580.578    0.000  580.578    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              358845426  528.598    0.000  528.598    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               33380964  518.711    0.000  518.711    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              119217750  510.077    0.000  510.077    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               59608875  498.605    0.000  498.605    0.000 {built-in method clamp}
               33380964  496.836    0.000  496.836    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               16690492  298.788    0.000  482.543    0.000 layer.py:167(NoRock_update)
               59608875   99.393    0.000  471.912    0.000 layers.py:729(isFree)
              787207682  276.390    0.000  450.451    0.000 {built-in method builtins.isinstance}
               59608875  448.265    0.000  448.265    0.000 {built-in method log}
               16094398  446.242    0.000  446.242    0.000 {built-in method tensor}
              178826650  128.395    0.000  439.736    0.000 {built-in method builtins.all}
               59608875  430.940    0.000  430.940    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              180942037  405.522    0.000  405.522    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               59608875  395.666    0.000  395.666    0.000 {built-in method all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601861: <Diamonds2_option_critic_1> in cluster <dcc> Done

Job <Diamonds2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:08 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:09 2021
Terminated at Sun May  2 21:36:14 2021
Results reported at Sun May  2 21:36:14 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258256.28 sec.
    Max Memory :                                 1030 MB
    Average Memory :                             1009.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15354.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258914 sec.
    Turnaround time :                            258906 sec.

The output (if any) is above this job summary.

