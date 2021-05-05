
# Parameters

    Name :                      Attempt2_SuperLevel2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      49716201330 function calls (48247625837 primitive calls) in 258900.63 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.625 258900.625 {built-in method builtins.exec}
                      1    0.342    0.342 258900.625 258900.625 <string>:1(<module>)
                      1 5639.705 5639.705 258900.283 258900.283 optionCritic.py:195(option_critic_run)
               52225275 9337.597    0.000 112835.899    0.002 optionCritic.py:143(actor_loss_fn)
        1939321611/477536175 10018.526    0.000 111974.193    0.000 module.py:866(_call_impl)
              162420604  846.375    0.000 104671.038    0.001 optionCritic.py:70(get_state)
              162420604 2275.672    0.000 101339.986    0.001 container.py:117(forward)
                2089011   16.032    0.000 75227.697    0.036 tensor.py:195(backward)
                2089011   21.175    0.000 75211.335    0.036 __init__.py:68(backward)
                2089011 75140.085    0.036 75140.085    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              324841208  917.846    0.000 64487.900    0.000 conv.py:398(forward)
              324841208  612.599    0.000 63140.133    0.000 conv.py:390(_conv_forward)
              324841208 62527.534    0.000 62527.534    0.000 {built-in method conv2d}
              639956779 1528.002    0.000 21283.273    0.000 linear.py:93(forward)
              639956779  635.194    0.000 19000.996    0.000 functional.py:1737(linear)
               52225275 3116.966    0.000 18459.907    0.000 optionCritic.py:91(get_action)
              639956779 18220.493    0.000 18220.493    0.000 {built-in method torch._C._nn.linear}
               52225275 1245.426    0.000 14924.112    0.000 optionCritic.py:80(predict_option_termination)
                2089011   43.877    0.000 8499.945    0.004 optimizer.py:84(wrapper)
                2089011   25.541    0.000 8326.468    0.004 grad_mode.py:24(decorate_context)
                2089011  115.133    0.000 8252.638    0.004 rmsprop.py:56(step)
                2089011  120.691    0.000 8004.259    0.004 _functional.py:203(rmsprop)
              104450550 1303.467    0.000 7857.353    0.000 distribution.py:34(__init__)
              487261812  532.134    0.000 6965.622    0.000 activation.py:713(forward)
              487261812  531.543    0.000 6433.487    0.000 functional.py:1364(leaky_relu)
               52225275  537.775    0.000 6400.243    0.000 bernoulli.py:34(__init__)
               52225275  525.832    0.000 6193.570    0.000 categorical.py:115(log_prob)
              487261812 5802.224    0.000 5802.224    0.000 {built-in method torch._C._nn.leaky_relu}
                2089011   13.188    0.000 5588.656    0.003 game.py:42(step)
                2089011   17.986    0.000 5427.412    0.003 layers.py:827(step)
              157917494  366.901    0.000 5377.806    0.000 optionCritic.py:77(get_Q)
               52225275  695.279    0.000 5148.748    0.000 categorical.py:49(__init__)
                 522252   89.259    0.000 4924.922    0.009 optionCritic.py:116(critic_loss_fn)
              104972802  407.098    0.000 4343.876    0.000 optionCritic.py:88(get_terminations)
               29246148 4190.849    0.000 4190.849    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2089011   82.457    0.000 3854.303    0.002 layers.py:17(step)
               52225275  252.769    0.000 3762.860    0.000 layer.py:106(move)
               52225275 2117.543    0.000 3143.097    0.000 constraints.py:398(check)
               29246148 2780.688    0.000 2780.688    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52225275  396.680    0.000 2631.735    0.000 layers.py:844(check)
               52225275  436.780    0.000 2532.319    0.000 distribution.py:240(_validate_sample)
               52225275 2262.118    0.000 2262.118    0.000 constraints.py:364(check)
               52225275  494.161    0.000 2240.567    0.000 bernoulli.py:86(sample)
              365576925 2020.002    0.000 2020.002    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              162420604  224.759    0.000 1997.435    0.000 activation.py:101(forward)
             2511854342 1937.991    0.000 1938.150    0.000 module.py:934(__getattr__)
              162420604  190.910    0.000 1772.676    0.000 functional.py:1195(relu)
               52225275  885.889    0.000 1704.164    0.000 categorical.py:123(entropy)
               52225275 1643.283    0.000 1643.283    0.000 constraints.py:249(check)
              162420604  186.538    0.000 1594.054    0.000 flatten.py:39(forward)
              157720329  218.713    0.000 1589.946    0.000 tensor.py:525(__rsub__)
              104450550  567.631    0.000 1581.101    0.000 functional.py:46(broadcast_tensors)
               52225275  371.017    0.000 1558.267    0.000 utils.py:11(broadcast_all)
              162420604 1554.986    0.000 1554.986    0.000 {built-in method relu}
                2089012  173.948    0.000 1548.238    0.001 layers.py:793(update)
              156675825  214.624    0.000 1533.222    0.000 utils.py:106(__get__)
              162420604 1407.515    0.000 1407.515    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              157720329 1342.814    0.000 1342.814    0.000 {built-in method rsub}
               22979121   55.135    0.000 1315.033    0.000 tensor.py:575(__iter__)
              104972802 1311.257    0.000 1311.257    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               22979121 1226.010    0.000 1226.010    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              157198077 1219.638    0.000 1219.638    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               52225275  334.948    0.000 1214.726    0.000 categorical.py:108(sample)
             1962300732 1207.138    0.000 1207.138    0.000 {built-in method torch._C._get_tracing_state}
               52225275   62.188    0.000 1156.199    0.000 categorical.py:88(logits)
             8603284135 1090.338    0.000 1107.710    0.000 {built-in method builtins.len}
               52225275   67.193    0.000 1094.011    0.000 utils.py:82(probs_to_logits)
              156675825 1069.311    0.000 1069.311    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 522252  836.922    0.002 1054.762    0.002 replaybuffer.py:42(sample_option_critic)
              156675825  973.258    0.000  973.258    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7919707048  934.396    0.000  934.396    0.000 {method 'values' of 'collections.OrderedDict' objects}
              104450550  851.931    0.000  851.931    0.000 {built-in method broadcast_tensors}
               52225275  782.785    0.000  782.785    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               52225275  133.228    0.000  725.757    0.000 layers.py:838(isFree)
                2089011   78.159    0.000  678.521    0.000 replaybuffer.py:34(save_option_critic)
               52225275  638.261    0.000  638.261    0.000 {built-in method bernoulli}
              158242581  633.088    0.000  633.088    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               52225275  137.856    0.000  631.545    0.000 utils.py:77(clamp_probs)
                2089011  102.355    0.000  592.817    0.000 optimizer.py:189(zero_grad)
              453260051  490.627    0.000  592.529    0.000 layer.py:103(isFree)
               22979132  340.554    0.000  569.304    0.000 layer.py:159(update)
              156675850  161.865    0.000  561.558    0.000 {built-in method builtins.all}
               52225275  399.445    0.000  545.250    0.000 layers.py:471(check)
               52225275  539.490    0.000  539.490    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              314396154  523.853    0.000  523.853    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              689698784  301.050    0.000  512.398    0.000 {built-in method builtins.isinstance}
               52422440  499.787    0.000  499.787    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               52225275  493.689    0.000  493.689    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
             1439534412  329.993    0.000  478.782    0.000 enum.py:646(__hash__)
              104450550  452.324    0.000  452.324    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               14100826  439.622    0.000  439.622    0.000 {built-in method tensor}
               52225275  429.798    0.000  429.798    0.000 {built-in method clamp}
              156877192  423.360    0.000  423.360    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               52225275  395.272    0.000  395.272    0.000 {built-in method log}
               52225275  240.031    0.000  392.507    0.000 layers.py:246(check)
               52225275  280.110    0.000  385.279    0.000 layers.py:77(check)
              162420618  381.806    0.000  381.806    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               52225275  372.300    0.000  372.300    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               54314312  200.372    0.000  361.474    0.000 grad_mode.py:119(__enter__)
               29246148  360.571    0.000  360.571    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 239, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606132: <Attempt2_SuperLevel2_option_critic_1> in cluster <dcc> Exited

Job <Attempt2_SuperLevel2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:12 2021
Terminated at Thu May  6 01:28:32 2021
Results reported at Thu May  6 01:28:32 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258265.31 sec.
    Max Memory :                                 1178 MB
    Average Memory :                             1156.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15206.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                7
    Run time :                                   258947 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

