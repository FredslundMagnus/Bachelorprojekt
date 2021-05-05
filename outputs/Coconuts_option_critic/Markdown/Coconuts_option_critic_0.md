[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Coconuts_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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


      33455698927 function calls (32408016843 primitive calls) in 258900.45 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.453 258900.453 {built-in method builtins.exec}
                      1    0.307    0.307 258900.453 258900.453 <string>:1(<module>)
                      1 3750.713 3750.713 258900.145 258900.145 optionCritic.py:195(option_critic_run)
        1383766079/340927952 10094.953    0.000 105604.496    0.000 module.py:866(_call_impl)
               37257525 9787.146    0.000 104300.256    0.003 optionCritic.py:143(actor_loss_fn)
              115870903  749.419    0.000 96567.246    0.001 optionCritic.py:70(get_state)
              115870903 2723.005    0.000 93453.049    0.001 container.py:117(forward)
                1490301   11.983    0.000 75965.534    0.051 tensor.py:195(backward)
                1490301   13.313    0.000 75953.267    0.051 __init__.py:68(backward)
                1490301 75903.340    0.051 75903.340    0.051 {method 'run_backward' of 'torch._C._EngineBase' objects}
              231741806  914.106    0.000 56025.595    0.000 conv.py:398(forward)
              231741806  378.007    0.000 54774.790    0.000 conv.py:390(_conv_forward)
              231741806 54396.783    0.000 54396.783    0.000 {built-in method conv2d}
               37257525 3840.215    0.000 22808.440    0.001 optionCritic.py:91(get_action)
              456798855 1602.560    0.000 21340.030    0.000 linear.py:93(forward)
              456798855  580.192    0.000 19122.455    0.000 functional.py:1737(linear)
              456798855 18422.644    0.000 18422.644    0.000 {built-in method torch._C._nn.linear}
                1490301   31.795    0.000 16157.820    0.011 optimizer.py:84(wrapper)
                1490301   18.032    0.000 16031.085    0.011 grad_mode.py:24(decorate_context)
                1490301  102.069    0.000 15980.845    0.011 rmsprop.py:56(step)
                1490301  159.945    0.000 15765.935    0.011 _functional.py:203(rmsprop)
               20864208 13167.408    0.001 13167.408    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37257525 1189.364    0.000 12672.818    0.000 optionCritic.py:80(predict_option_termination)
               74515050 1072.394    0.000 8295.472    0.000 distribution.py:34(__init__)
              347612709  410.317    0.000 7860.991    0.000 activation.py:713(forward)
               37257525  626.798    0.000 7492.797    0.000 categorical.py:115(log_prob)
              347612709  430.662    0.000 7450.675    0.000 functional.py:1364(leaky_relu)
              347612709 6930.913    0.000 6930.913    0.000 {built-in method torch._C._nn.leaky_relu}
               37257525  880.897    0.000 6720.991    0.000 categorical.py:49(__init__)
              112911899  448.921    0.000 6293.615    0.000 optionCritic.py:77(get_Q)
                 372575   85.155    0.000 6061.335    0.016 optionCritic.py:116(critic_loss_fn)
               74887625  448.578    0.000 5125.147    0.000 optionCritic.py:88(get_terminations)
               37257525  273.989    0.000 4437.745    0.000 bernoulli.py:34(__init__)
               37257525 2783.113    0.000 4178.902    0.000 constraints.py:398(check)
                1490301    9.329    0.000 3694.573    0.002 game.py:41(step)
                1490301   12.726    0.000 3581.674    0.002 layers.py:718(step)
               37257525  465.333    0.000 3157.917    0.000 distribution.py:240(_validate_sample)
              115870903  165.087    0.000 2236.924    0.000 activation.py:101(forward)
                1490301   68.392    0.000 2213.287    0.001 layers.py:17(step)
               37257525 1075.532    0.000 2205.866    0.000 categorical.py:123(entropy)
               37257525  223.192    0.000 2139.816    0.000 layer.py:98(move)
               37257525 2135.016    0.000 2135.016    0.000 constraints.py:249(check)
              115870903  142.366    0.000 2071.838    0.000 functional.py:1195(relu)
               37257525 1989.430    0.000 1989.430    0.000 constraints.py:364(check)
              115870903 1901.195    0.000 1901.195    0.000 {built-in method relu}
              111772575  218.957    0.000 1828.629    0.000 utils.py:106(__get__)
             1400159390 1793.571    0.000 1793.571    0.000 {built-in method torch._C._get_tracing_state}
              260802675 1772.060    0.000 1772.060    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               37257525  303.858    0.000 1687.024    0.000 bernoulli.py:86(sample)
             1792718123 1654.903    0.000 1655.054    0.000 module.py:934(__getattr__)
              112517725  180.310    0.000 1642.125    0.000 tensor.py:525(__rsub__)
              115870903  107.976    0.000 1559.658    0.000 flatten.py:39(forward)
              111772575 1558.739    0.000 1558.739    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              115870903 1451.682    0.000 1451.682    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37257525   73.380    0.000 1445.333    0.000 categorical.py:88(logits)
              112145150 1429.930    0.000 1429.930    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              112517725 1429.601    0.000 1429.601    0.000 {built-in method rsub}
               37257525  368.550    0.000 1424.182    0.000 categorical.py:108(sample)
               37257525  229.590    0.000 1405.729    0.000 layers.py:735(check)
               37257525   74.914    0.000 1371.952    0.000 utils.py:82(probs_to_logits)
                1490302  145.430    0.000 1349.869    0.001 layers.py:684(update)
               20864208 1213.127    0.000 1213.127    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               74515050  381.992    0.000 1204.959    0.000 functional.py:46(broadcast_tensors)
               74887625 1180.006    0.000 1180.006    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              111772575 1070.207    0.000 1070.207    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               16393311   45.660    0.000 1040.075    0.000 tensor.py:575(__iter__)
             5980214259 1011.945    0.000 1025.012    0.000 {built-in method builtins.len}
               16393311  959.308    0.000  959.308    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5650935219  903.622    0.000  903.622    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37257525  166.130    0.000  840.046    0.000 utils.py:11(broadcast_all)
               37257525  131.764    0.000  837.759    0.000 utils.py:77(clamp_probs)
               37257525  802.238    0.000  802.238    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               74515050  721.355    0.000  721.355    0.000 {built-in method broadcast_tensors}
                1490301   74.278    0.000  709.091    0.000 replaybuffer.py:34(save_option_critic)
               37257525  705.994    0.000  705.994    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              112890300  703.859    0.000  703.859    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                 372575  523.410    0.001  681.151    0.002 replaybuffer.py:42(sample_option_critic)
               37257525  673.101    0.000  673.101    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               12038042  297.570    0.000  626.510    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              224290300  623.232    0.000  623.232    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37257525  613.783    0.000  613.783    0.000 {built-in method clamp}
               74515050  595.184    0.000  595.184    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37651699  568.062    0.000  568.062    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37257525  534.759    0.000  534.759    0.000 {built-in method bernoulli}
                1490301   90.609    0.000  470.608    0.000 optimizer.py:189(zero_grad)
               37257525  466.788    0.000  466.788    0.000 {built-in method all}
               37257525  459.280    0.000  459.280    0.000 {built-in method log}
               37257525  343.091    0.000  458.418    0.000 layers.py:471(check)
               37257525  451.279    0.000  451.279    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               20864208  449.732    0.000  449.732    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 394199    7.413    0.000  435.696    0.001 layers.py:740(restart)
               10432114  263.018    0.000  401.021    0.000 layer.py:151(update)
               20864208  390.663    0.000  390.663    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               20864208  385.060    0.000  385.060    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               37257525   86.694    0.000  380.466    0.000 layers.py:729(isFree)
                 394199    3.532    0.000  367.595    0.001 level.py:8(__init__)
               37257525  273.276    0.000  360.283    0.000 layers.py:77(check)
                 394199   25.997    0.000  341.742    0.001 levels.py:262(generate)
               37257525  336.540    0.000  336.540    0.000 {built-in method multinomial}
               12038042   18.521    0.000  328.940    0.000 <__array_function__ internals>:2(prod)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601881: <Coconuts_option_critic_0> in cluster <dcc> Done

Job <Coconuts_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:21 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:23 2021
Terminated at Sun May  2 21:36:25 2021
Results reported at Sun May  2 21:36:25 2021

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

    CPU time :                                   258894.08 sec.
    Max Memory :                                 867 MB
    Average Memory :                             858.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15517.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258961 sec.
    Turnaround time :                            258904 sec.

The output (if any) is above this job summary.

