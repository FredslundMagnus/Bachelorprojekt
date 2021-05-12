
# Parameters

    Name :                      Attempt6_Diamonds4_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal7
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      15764151154 function calls (15250160399 primitive calls) in 258900.94 seconds

##    Ordered by: cumulative time
   List reduced from 431 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.940 258900.940 {built-in method builtins.exec}
                      1    0.306    0.306 258900.940 258900.940 <string>:1(<module>)
                      1 1787.263 1787.263 258900.635 258900.635 optionCritic.py:195(option_critic_run)
                 576222    4.324    0.000 196568.025    0.341 tensor.py:195(backward)
                 576222    5.287    0.000 196563.618    0.341 __init__.py:68(backward)
                 576222 196546.471    0.341 196546.471    0.341 {method 'run_backward' of 'torch._C._EngineBase' objects}
        680159606/168042308 3144.301    0.000 39413.395    0.000 module.py:866(_call_impl)
               18439104 2659.288    0.000 37634.747    0.002 optionCritic.py:143(actor_loss_fn)
               56901922  257.309    0.000 36994.556    0.001 optionCritic.py:70(get_state)
               56901922  741.965    0.000 35968.081    0.001 container.py:117(forward)
              113803844  294.688    0.000 23515.814    0.000 conv.py:398(forward)
              113803844  170.822    0.000 23101.693    0.000 conv.py:390(_conv_forward)
              113803844 22930.871    0.000 22930.871    0.000 {built-in method conv2d}
              224944230  520.107    0.000 7454.171    0.000 linear.py:93(forward)
              224944230  216.052    0.000 6721.562    0.000 functional.py:1737(linear)
              224944230 6454.754    0.000 6454.754    0.000 {built-in method torch._C._nn.linear}
               18439104 1047.144    0.000 6309.138    0.000 optionCritic.py:91(get_action)
               18439104  365.460    0.000 4357.036    0.000 optionCritic.py:80(predict_option_termination)
                 576222   12.049    0.000 4231.542    0.007 optimizer.py:84(wrapper)
                 576222    6.616    0.000 4185.784    0.007 grad_mode.py:24(decorate_context)
                 576222   33.874    0.000 4167.027    0.007 adam.py:55(step)
                 576222  198.493    0.000 4095.969    0.007 _functional.py:53(adam)
               36878208  370.196    0.000 2468.042    0.000 distribution.py:34(__init__)
              170705766  170.165    0.000 2270.942    0.000 activation.py:713(forward)
               18439104  179.334    0.000 2114.393    0.000 categorical.py:115(log_prob)
              170705766  174.273    0.000 2100.777    0.000 functional.py:1364(leaky_relu)
                 144055   22.501    0.000 2015.228    0.014 optionCritic.py:116(critic_loss_fn)
              170705766 1890.892    0.000 1890.892    0.000 {built-in method torch._C._nn.leaky_relu}
               18439104  239.619    0.000 1772.369    0.000 categorical.py:49(__init__)
               55679019  123.718    0.000 1769.234    0.000 optionCritic.py:77(get_Q)
               18439104  133.997    0.000 1703.442    0.000 bernoulli.py:34(__init__)
               37022263  129.971    0.000 1385.637    0.000 optionCritic.py:88(get_terminations)
               18439104  730.967    0.000 1085.225    0.000 constraints.py:398(check)
                 576222    3.209    0.000 1013.667    0.002 game.py:42(step)
                 576222    5.061    0.000  980.374    0.002 layers.py:827(step)
               16134204  913.716    0.000  913.716    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18439104  147.109    0.000  850.851    0.000 distribution.py:240(_validate_sample)
                8067102  842.389    0.000  842.389    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8067102  666.398    0.000  666.398    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               56901922   72.865    0.000  660.680    0.000 activation.py:101(forward)
               18439104  653.358    0.000  653.358    0.000 constraints.py:364(check)
               18439104  122.997    0.000  636.717    0.000 bernoulli.py:86(sample)
                 576222   24.882    0.000  621.439    0.001 layers.py:17(step)
               18439104   44.112    0.000  594.209    0.000 layer.py:106(move)
               56901922   64.366    0.000  587.815    0.000 functional.py:1195(relu)
               18439104  302.369    0.000  582.142    0.000 categorical.py:123(entropy)
              882491643  565.225    0.000  565.266    0.000 module.py:934(__getattr__)
               18439104  552.396    0.000  552.396    0.000 constraints.py:249(check)
              129073728  537.942    0.000  537.942    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               55317312   74.300    0.000  535.157    0.000 utils.py:106(__get__)
               56901922  513.727    0.000  513.727    0.000 {built-in method relu}
               56901922   52.421    0.000  504.483    0.000 flatten.py:39(forward)
               55605422   58.198    0.000  499.435    0.000 tensor.py:525(__rsub__)
                8067102  497.088    0.000  497.088    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16134204  488.057    0.000  488.057    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8067102  486.786    0.000  486.786    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               36878208  160.560    0.000  463.816    0.000 functional.py:46(broadcast_tensors)
               56901922  452.062    0.000  452.062    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               55605422  431.260    0.000  431.260    0.000 {built-in method rsub}
              686498048  414.101    0.000  414.101    0.000 {built-in method torch._C._get_tracing_state}
               18439104  113.646    0.000  411.285    0.000 categorical.py:108(sample)
               18439104   21.103    0.000  404.961    0.000 categorical.py:88(logits)
                6338442   14.212    0.000  399.051    0.000 tensor.py:575(__iter__)
               37022263  397.619    0.000  397.619    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               55461367  385.932    0.000  385.932    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               18439104   77.412    0.000  385.028    0.000 utils.py:11(broadcast_all)
               18439104   22.570    0.000  383.858    0.000 utils.py:82(probs_to_logits)
                6338442  375.923    0.000  375.923    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               55317312  366.582    0.000  366.582    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             2938639734  362.557    0.000  366.446    0.000 {built-in method builtins.len}
                 576223   49.172    0.000  351.337    0.001 layers.py:793(update)
               18439104   75.835    0.000  350.170    0.000 layers.py:844(check)
               55317312  308.420    0.000  308.420    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             2777540346  307.371    0.000  307.371    0.000 {method 'values' of 'collections.OrderedDict' objects}
               18439104  279.869    0.000  279.869    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 144055  221.218    0.002  274.913    0.002 replaybuffer.py:42(sample_option_critic)
               36878208  244.832    0.000  244.832    0.000 {built-in method broadcast_tensors}
               18439104   49.792    0.000  227.753    0.000 utils.py:77(clamp_probs)
                 576222   26.081    0.000  221.893    0.000 replaybuffer.py:34(save_option_critic)
               55749477  204.905    0.000  204.905    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               18439104  197.260    0.000  197.260    0.000 {built-in method bernoulli}
               18439104  180.832    0.000  180.832    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               18439104  177.960    0.000  177.960    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               18512701  172.360    0.000  172.360    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              110922734  162.410    0.000  162.410    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               18439104   35.879    0.000  160.317    0.000 layers.py:838(isFree)
               36878208  154.494    0.000  154.494    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               18439104  148.473    0.000  148.473    0.000 {built-in method clamp}
                 576222   26.424    0.000  147.699    0.000 optimizer.py:189(zero_grad)
               18439104  133.535    0.000  133.535    0.000 {built-in method log}
               18439104  130.146    0.000  130.146    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                4033561   74.691    0.000  126.470    0.000 layer.py:175(NoRock_update)
              242679863   86.636    0.000  125.140    0.000 {built-in method builtins.isinstance}
              125679310  102.874    0.000  124.439    0.000 layer.py:103(isFree)
               18439104  117.982    0.000  117.982    0.000 {built-in method all}
               56901936  114.455    0.000  114.455    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               18439104  104.959    0.000  104.959    0.000 {built-in method multinomial}
                3889501  101.636    0.000  101.636    0.000 {built-in method tensor}
               55317344   34.632    0.000   97.867    0.000 {built-in method builtins.all}
               55392092   96.571    0.000   96.571    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624156: <Attempt6_Diamonds4_option_critic_0> in cluster <dcc> Done

Job <Attempt6_Diamonds4_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:27 2021
Terminated at Wed May 12 01:17:34 2021
Results reported at Wed May 12 01:17:34 2021

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

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258289.08 sec.
    Max Memory :                                 868 MB
    Average Memory :                             856.18 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15516.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258907 sec.

The output (if any) is above this job summary.

