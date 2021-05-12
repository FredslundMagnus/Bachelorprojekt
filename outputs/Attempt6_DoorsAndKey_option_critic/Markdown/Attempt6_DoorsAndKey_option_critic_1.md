
# Parameters

    Name :                      Attempt6_DoorsAndKey_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      16369336072 function calls (15825170832 primitive calls) in 258900.79 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.786 258900.786 {built-in method builtins.exec}
                      1    0.356    0.356 258900.786 258900.786 <string>:1(<module>)
                      1 2230.873 2230.873 258900.430 258900.430 optionCritic.py:195(option_critic_run)
                 610050    5.201    0.000 190066.413    0.312 tensor.py:195(backward)
                 610050    6.639    0.000 190061.121    0.312 __init__.py:68(backward)
                 610050 190039.731    0.312 190039.731    0.312 {method 'run_backward' of 'torch._C._EngineBase' objects}
        720193532/178011599 3555.446    0.000 43225.845    0.000 module.py:866(_call_impl)
               19521600 3064.679    0.000 41859.426    0.002 optionCritic.py:143(actor_loss_fn)
               60242437  284.445    0.000 40522.973    0.001 optionCritic.py:70(get_state)
               60242437  817.509    0.000 39366.176    0.001 container.py:117(forward)
              120484874  322.955    0.000 24508.732    0.000 conv.py:398(forward)
              120484874  222.804    0.000 24042.903    0.000 conv.py:390(_conv_forward)
              120484874 23820.099    0.000 23820.099    0.000 {built-in method conv2d}
              238254036  566.133    0.000 9277.956    0.000 linear.py:93(forward)
              238254036  233.007    0.000 8463.533    0.000 functional.py:1737(linear)
              238254036 8176.842    0.000 8176.842    0.000 {built-in method torch._C._nn.linear}
               19521600 1153.846    0.000 6833.289    0.000 optionCritic.py:91(get_action)
               19521600  456.112    0.000 5350.094    0.000 optionCritic.py:80(predict_option_termination)
                 610050   14.902    0.000 3970.533    0.007 optimizer.py:84(wrapper)
                 610050    8.247    0.000 3915.565    0.006 grad_mode.py:24(decorate_context)
                 610050   38.736    0.000 3892.432    0.006 adam.py:55(step)
                 610050  247.876    0.000 3811.990    0.006 _functional.py:53(adam)
               39043200  477.176    0.000 2866.315    0.000 distribution.py:34(__init__)
              180727311  215.771    0.000 2579.940    0.000 activation.py:713(forward)
              180727311  194.045    0.000 2364.169    0.000 functional.py:1364(leaky_relu)
               19521600  192.144    0.000 2261.336    0.000 categorical.py:115(log_prob)
               19521600  182.037    0.000 2212.926    0.000 bernoulli.py:34(__init__)
              180727311 2131.809    0.000 2131.809    0.000 {built-in method torch._C._nn.leaky_relu}
                 152512   27.565    0.000 2086.064    0.014 optionCritic.py:116(critic_loss_fn)
               59051850  136.294    0.000 1963.820    0.000 optionCritic.py:77(get_Q)
               19521600  264.547    0.000 1920.698    0.000 categorical.py:49(__init__)
               39195712  146.781    0.000 1574.828    0.000 optionCritic.py:88(get_terminations)
               19521600  789.702    0.000 1167.726    0.000 constraints.py:398(check)
                 610050    3.276    0.000 1019.590    0.002 game.py:42(step)
                 610050    6.013    0.000  976.917    0.002 layers.py:827(step)
               19521600  158.223    0.000  912.879    0.000 distribution.py:240(_validate_sample)
               19521600  178.357    0.000  836.933    0.000 bernoulli.py:86(sample)
               17081388  817.512    0.000  817.512    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               19521600  794.486    0.000  794.486    0.000 constraints.py:364(check)
               60242437   76.822    0.000  731.506    0.000 activation.py:101(forward)
                8540694  729.013    0.000  729.013    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8540694  664.925    0.000  664.925    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60242437   72.425    0.000  654.684    0.000 functional.py:1195(relu)
              934611992  651.753    0.000  651.798    0.000 module.py:934(__getattr__)
              136651200  632.360    0.000  632.360    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               19521600  325.392    0.000  629.224    0.000 categorical.py:123(entropy)
               19521600  593.171    0.000  593.171    0.000 constraints.py:249(check)
               60242437  571.723    0.000  571.723    0.000 {built-in method relu}
               58869824   73.848    0.000  569.314    0.000 tensor.py:525(__rsub__)
               58564800   78.513    0.000  568.985    0.000 utils.py:106(__get__)
               60242437   60.120    0.000  562.743    0.000 flatten.py:39(forward)
               39043200  205.146    0.000  557.049    0.000 functional.py:46(broadcast_tensors)
                 610050   27.772    0.000  534.284    0.001 layers.py:17(step)
               19521600  109.512    0.000  513.917    0.000 utils.py:11(broadcast_all)
               19521600   48.994    0.000  504.003    0.000 layer.py:106(move)
               60242437  502.623    0.000  502.623    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6710550   16.518    0.000  490.862    0.000 tensor.py:575(__iter__)
                8540694  486.104    0.000  486.104    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58869824  485.113    0.000  485.113    0.000 {built-in method rsub}
                6710550  464.452    0.000  464.452    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               39195712  460.657    0.000  460.657    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               19521600  122.761    0.000  449.359    0.000 categorical.py:108(sample)
               58717312  444.293    0.000  444.293    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               17081388  434.574    0.000  434.574    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 610051   57.279    0.000  433.495    0.001 layers.py:793(update)
               19521600   22.466    0.000  431.560    0.000 categorical.py:88(logits)
                8540694  428.339    0.000  428.339    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              726904082  426.748    0.000  426.748    0.000 {built-in method torch._C._get_tracing_state}
               19521600   23.949    0.000  409.094    0.000 utils.py:82(probs_to_logits)
             3091839956  390.678    0.000  395.097    0.000 {built-in method builtins.len}
               58564800  394.817    0.000  394.817    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               58564800  358.739    0.000  358.739    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                 152512  289.264    0.002  351.703    0.002 replaybuffer.py:42(sample_option_critic)
             2941016565  333.519    0.000  333.519    0.000 {method 'values' of 'collections.OrderedDict' objects}
               19521600  309.921    0.000  309.921    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               39043200  290.308    0.000  290.308    0.000 {built-in method broadcast_tensors}
                 610050   29.219    0.000  264.651    0.000 replaybuffer.py:34(save_option_critic)
               19521600   49.486    0.000  240.546    0.000 utils.py:77(clamp_probs)
               19521600  236.447    0.000  236.447    0.000 {built-in method bernoulli}
               19521600   71.591    0.000  232.902    0.000 layers.py:844(check)
               59022336  228.175    0.000  228.175    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
              117434624  192.151    0.000  192.151    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               19521600  191.060    0.000  191.060    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               19521600  188.666    0.000  188.666    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               19703626  188.237    0.000  188.237    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 610050   30.002    0.000  180.974    0.000 optimizer.py:189(zero_grad)
               19521600   34.042    0.000  178.304    0.000 layers.py:838(isFree)
               39043200  167.675    0.000  167.675    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               19521600  163.054    0.000  163.054    0.000 {built-in method clamp}
              256926610  105.414    0.000  162.798    0.000 {built-in method builtins.isinstance}
               58748077  161.423    0.000  161.423    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               19521600  144.599    0.000  144.599    0.000 {built-in method log}
              110077277  118.444    0.000  144.261    0.000 layer.py:103(isFree)
               58564832   44.442    0.000  141.537    0.000 {built-in method builtins.all}
                4117840  139.736    0.000  139.736    0.000 {built-in method tensor}
               19521600  137.287    0.000  137.287    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               20131676   67.682    0.000  130.130    0.000 grad_mode.py:119(__enter__)
               60242451  128.298    0.000  128.298    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                3660306   76.908    0.000  127.590    0.000 layer.py:175(NoRock_update)
               19521600  126.167    0.000  126.167    0.000 {built-in method all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624175: <Attempt6_DoorsAndKey_option_critic_1> in cluster <dcc> Done

Job <Attempt6_DoorsAndKey_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:30 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:30 2021
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

    CPU time :                                   258288.05 sec.
    Max Memory :                                 789 MB
    Average Memory :                             783.87 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15595.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258904 sec.

The output (if any) is above this job summary.

