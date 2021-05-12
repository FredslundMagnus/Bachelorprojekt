
# Parameters

    Name :                      Attempt5_Maze_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Maze
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


      15745003032 function calls (15233009086 primitive calls) in 258900.37 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258902.024 258902.024 {built-in method builtins.exec}
                      1    0.329    0.329 258902.024 258902.024 <string>:1(<module>)
                      1 1797.923 1797.923 258901.694 258901.694 optionCritic.py:195(option_critic_run)
                 573984    4.937    0.000 196565.678    0.342 tensor.py:195(backward)
                 573984    6.231    0.000 196560.639    0.342 __init__.py:68(backward)
                 573984 196540.361    0.342 196540.361    0.342 {method 'run_backward' of 'torch._C._EngineBase' objects}
        677522089/167393800 3283.927    0.000 37215.589    0.000 module.py:866(_call_impl)
               18367488 3008.433    0.000 37005.707    0.002 optionCritic.py:143(actor_loss_fn)
               56680921  266.540    0.000 34639.343    0.001 optionCritic.py:70(get_state)
               56680921  752.517    0.000 33563.754    0.001 container.py:117(forward)
              113361842  314.464    0.000 20785.392    0.000 conv.py:398(forward)
              113361842  167.384    0.000 20344.938    0.000 conv.py:390(_conv_forward)
              113361842 20177.554    0.000 20177.554    0.000 {built-in method conv2d}
              224074721  545.321    0.000 7595.222    0.000 linear.py:93(forward)
               18367488 1179.590    0.000 7036.894    0.000 optionCritic.py:91(get_action)
              224074721  211.563    0.000 6829.245    0.000 functional.py:1737(linear)
              224074721 6562.100    0.000 6562.100    0.000 {built-in method torch._C._nn.linear}
                 573984   14.635    0.000 4828.282    0.008 optimizer.py:84(wrapper)
                 573984    7.705    0.000 4770.894    0.008 grad_mode.py:24(decorate_context)
                 573984   39.748    0.000 4749.001    0.008 adam.py:55(step)
                 573984  215.852    0.000 4665.291    0.008 _functional.py:53(adam)
               18367488  376.251    0.000 4540.244    0.000 optionCritic.py:80(predict_option_termination)
               36734976  392.615    0.000 2662.790    0.000 distribution.py:34(__init__)
              170042763  166.554    0.000 2351.090    0.000 activation.py:713(forward)
               18367488  195.421    0.000 2340.700    0.000 categorical.py:115(log_prob)
              170042763  180.547    0.000 2184.535    0.000 functional.py:1364(leaky_relu)
               18367488  259.118    0.000 1985.651    0.000 categorical.py:49(__init__)
              170042763 1967.656    0.000 1967.656    0.000 {built-in method torch._C._nn.leaky_relu}
               55466919  131.283    0.000 1885.912    0.000 optionCritic.py:77(get_Q)
               18367488  128.103    0.000 1711.655    0.000 bernoulli.py:34(__init__)
                 143496   23.622    0.000 1558.100    0.011 optionCritic.py:116(critic_loss_fn)
               36878472  133.066    0.000 1447.767    0.000 optionCritic.py:88(get_terminations)
                 573984    3.107    0.000 1233.910    0.002 game.py:42(step)
               18367488  826.307    0.000 1222.687    0.000 constraints.py:398(check)
                 573984    5.874    0.000 1195.815    0.002 layers.py:827(step)
               16071540 1039.728    0.000 1039.728    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                8035770  976.045    0.000  976.045    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18367488  167.506    0.000  947.927    0.000 distribution.py:240(_validate_sample)
                8035770  751.760    0.000  751.760    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 573984   27.531    0.000  708.697    0.001 layers.py:17(step)
               56680921   75.687    0.000  700.747    0.000 activation.py:101(forward)
               18367488   47.703    0.000  678.217    0.000 layer.py:106(move)
               18367488  125.400    0.000  677.705    0.000 bernoulli.py:86(sample)
               18367488  670.965    0.000  670.965    0.000 constraints.py:364(check)
               18367488  335.526    0.000  647.150    0.000 categorical.py:123(entropy)
               56680921   73.385    0.000  625.060    0.000 functional.py:1195(relu)
               18367488  608.650    0.000  608.650    0.000 constraints.py:249(check)
              879076569  597.656    0.000  597.706    0.000 module.py:934(__getattr__)
               55102464   79.774    0.000  587.385    0.000 utils.py:106(__get__)
              128572416  581.054    0.000  581.054    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8035770  568.949    0.000  568.949    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16071540  559.730    0.000  559.730    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8035770  549.546    0.000  549.546    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               56680921  541.345    0.000  541.345    0.000 {built-in method relu}
               56680921   56.024    0.000  538.411    0.000 flatten.py:39(forward)
               55389456   59.374    0.000  503.096    0.000 tensor.py:525(__rsub__)
               56680921  482.386    0.000  482.386    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 573985   59.966    0.000  478.490    0.001 layers.py:793(update)
               36734976  170.645    0.000  478.019    0.000 functional.py:46(broadcast_tensors)
               18367488  125.008    0.000  459.651    0.000 categorical.py:108(sample)
              683835913  453.267    0.000  453.267    0.000 {built-in method torch._C._get_tracing_state}
               18367488   23.361    0.000  445.806    0.000 categorical.py:88(logits)
                6313824   15.167    0.000  438.936    0.000 tensor.py:575(__iter__)
               55389456  433.477    0.000  433.477    0.000 {built-in method rsub}
               18367488   24.566    0.000  422.444    0.000 utils.py:82(probs_to_logits)
                6313824  413.727    0.000  413.727    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               55102464  406.824    0.000  406.824    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               55245960  405.510    0.000  405.510    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               36878472  400.835    0.000  400.835    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             2938216410  393.411    0.000  398.109    0.000 {built-in method builtins.len}
               18367488   94.377    0.000  388.829    0.000 layers.py:844(check)
               18367488   83.031    0.000  384.397    0.000 utils.py:11(broadcast_all)
               55102464  333.496    0.000  333.496    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             2766769277  329.003    0.000  329.003    0.000 {method 'values' of 'collections.OrderedDict' objects}
               18367488  306.155    0.000  306.155    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 143496  237.780    0.002  297.365    0.002 replaybuffer.py:42(sample_option_critic)
               36734976  259.617    0.000  259.617    0.000 {built-in method broadcast_tensors}
               18367488   49.795    0.000  249.617    0.000 utils.py:77(clamp_probs)
                 573984   28.138    0.000  242.785    0.000 replaybuffer.py:34(save_option_critic)
               55532952  213.303    0.000  213.303    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               18367488   43.285    0.000  208.842    0.000 layers.py:838(isFree)
               18367488  205.016    0.000  205.016    0.000 {built-in method bernoulli}
               18367488  201.425    0.000  201.425    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               18367488  199.822    0.000  199.822    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               18444951  184.071    0.000  184.071    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              110491920  175.146    0.000  175.146    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               36734976  172.047    0.000  172.047    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               18367488  165.579    0.000  165.579    0.000 {built-in method clamp}
              127742618  137.514    0.000  165.558    0.000 layer.py:103(isFree)
                 573984   28.967    0.000  164.607    0.000 optimizer.py:189(zero_grad)
                4591880   92.459    0.000  158.559    0.000 layer.py:175(NoRock_update)
               18367488  148.261    0.000  148.261    0.000 {built-in method log}
               18367488  144.819    0.000  144.819    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               18367488  134.269    0.000  134.269    0.000 {built-in method all}
               56680935  120.099    0.000  120.099    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                3874396  119.338    0.000  119.338    0.000 {built-in method tensor}
              242315491   79.398    0.000  119.047    0.000 {built-in method builtins.isinstance}
               18367488  117.327    0.000  117.327    0.000 {built-in method multinomial}
               18367488   69.670    0.000  116.598    0.000 layers.py:168(check)
               55102496   40.389    0.000  116.033    0.000 {built-in method builtins.all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618614: <Attempt5_Maze_option_critic_1> in cluster <dcc> Done

Job <Attempt5_Maze_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:27 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sat May  8 23:13:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:13:45 2021
Terminated at Tue May 11 23:09:02 2021
Results reported at Tue May 11 23:09:02 2021

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

    CPU time :                                   258290.48 sec.
    Max Memory :                                 942 MB
    Average Memory :                             922.79 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15442.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258972 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.

