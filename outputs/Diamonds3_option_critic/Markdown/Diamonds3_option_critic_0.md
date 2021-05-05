
# Parameters

    Name :                      Diamonds3_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      54221572476 function calls (52508832106 primitive calls) in 258900.53 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.534 258900.534 {built-in method builtins.exec}
                      1    0.377    0.377 258900.534 258900.534 <string>:1(<module>)
                      1 6281.442 6281.442 258900.157 258900.157 optionCritic.py:195(option_critic_run)
               60908250 9511.787    0.000 113197.135    0.002 optionCritic.py:143(actor_loss_fn)
        2261885091/557063178 10165.562    0.000 112790.816    0.000 module.py:866(_call_impl)
              189424657  823.454    0.000 105179.779    0.001 optionCritic.py:70(get_state)
              189424657 2282.654    0.000 101796.624    0.001 container.py:117(forward)
                2436330   19.781    0.000 71723.313    0.029 tensor.py:195(backward)
                2436330   24.732    0.000 71703.205    0.029 __init__.py:68(backward)
                2436330 71620.820    0.029 71620.820    0.029 {method 'run_backward' of 'torch._C._EngineBase' objects}
              378849314  958.783    0.000 64428.888    0.000 conv.py:398(forward)
              378849314  544.758    0.000 63074.073    0.000 conv.py:390(_conv_forward)
              378849314 62529.315    0.000 62529.315    0.000 {built-in method conv2d}
               60908250 3670.522    0.000 21441.977    0.000 optionCritic.py:91(get_action)
              746487835 1645.627    0.000 21085.838    0.000 linear.py:93(forward)
              746487835  646.243    0.000 18751.370    0.000 functional.py:1737(linear)
              746487835 17956.726    0.000 17956.726    0.000 {built-in method torch._C._nn.linear}
               60908250 1261.272    0.000 14558.161    0.000 optionCritic.py:80(predict_option_termination)
                2436330   57.037    0.000 8272.641    0.003 optimizer.py:84(wrapper)
              121816500 1293.981    0.000 8255.316    0.000 distribution.py:34(__init__)
                2436330   31.170    0.000 8066.252    0.003 grad_mode.py:24(decorate_context)
                2436330  141.565    0.000 7976.705    0.003 rmsprop.py:56(step)
                2436330  144.928    0.000 7679.109    0.003 _functional.py:203(rmsprop)
              568273971  536.564    0.000 7465.097    0.000 activation.py:713(forward)
               60908250  603.654    0.000 7079.125    0.000 categorical.py:115(log_prob)
              568273971  583.089    0.000 6928.533    0.000 functional.py:1364(leaky_relu)
              568273971 6233.153    0.000 6233.153    0.000 {built-in method torch._C._nn.leaky_relu}
               60908250  830.315    0.000 6002.625    0.000 categorical.py:49(__init__)
               60908250  479.464    0.000 5780.536    0.000 bernoulli.py:34(__init__)
              184304689  374.691    0.000 5620.510    0.000 optionCritic.py:77(get_Q)
                 609082   99.397    0.000 5070.077    0.008 optionCritic.py:116(critic_loss_fn)
              122425582  405.563    0.000 4399.664    0.000 optionCritic.py:88(get_terminations)
                2436330   12.064    0.000 4134.390    0.002 game.py:41(step)
                2436330   21.358    0.000 3983.992    0.002 layers.py:718(step)
               60908250 2455.124    0.000 3639.309    0.000 constraints.py:398(check)
               34108614 3635.343    0.000 3635.343    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60908250  503.592    0.000 2885.756    0.000 distribution.py:240(_validate_sample)
               34108614 2547.877    0.000 2547.877    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2436330   89.464    0.000 2367.453    0.001 layers.py:17(step)
               60908250  155.931    0.000 2269.711    0.000 layer.py:98(move)
               60908250  462.449    0.000 2193.749    0.000 bernoulli.py:86(sample)
               60908250 2124.312    0.000 2124.312    0.000 constraints.py:364(check)
              189424657  231.900    0.000 2123.139    0.000 activation.py:101(forward)
               60908250 1042.292    0.000 1998.908    0.000 categorical.py:123(entropy)
              189424657  224.225    0.000 1891.238    0.000 functional.py:1195(relu)
               60908250 1865.761    0.000 1865.761    0.000 constraints.py:249(check)
             2929870755 1839.683    0.000 1839.863    0.000 module.py:934(__getattr__)
              426357750 1805.705    0.000 1805.705    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              182724750  250.218    0.000 1773.079    0.000 utils.py:106(__get__)
              189424657  179.816    0.000 1643.602    0.000 flatten.py:39(forward)
              189424657 1637.328    0.000 1637.328    0.000 {built-in method relu}
              183942914  210.686    0.000 1599.071    0.000 tensor.py:525(__rsub__)
                2436331  206.579    0.000 1586.459    0.001 layers.py:684(update)
                 609082 1291.023    0.002 1540.332    0.003 replaybuffer.py:42(sample_option_critic)
              121816500  546.819    0.000 1523.426    0.000 functional.py:46(broadcast_tensors)
               26799630   61.482    0.000 1468.698    0.000 tensor.py:575(__iter__)
              189424657 1463.786    0.000 1463.786    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               60908250  294.380    0.000 1438.584    0.000 layers.py:735(check)
               60908250  398.598    0.000 1416.055    0.000 categorical.py:108(sample)
               26799630 1369.886    0.000 1369.886    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              183942914 1359.838    0.000 1359.838    0.000 {built-in method rsub}
               60908250   71.886    0.000 1338.760    0.000 categorical.py:88(logits)
               60908250  321.499    0.000 1330.919    0.000 utils.py:11(broadcast_all)
             2288684721 1318.467    0.000 1318.467    0.000 {built-in method torch._C._get_tracing_state}
               60908250   77.729    0.000 1266.874    0.000 utils.py:82(probs_to_logits)
              122425582 1264.637    0.000 1264.637    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              182724750 1243.621    0.000 1243.621    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              183333832 1242.705    0.000 1242.705    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             9845108620 1206.286    0.000 1224.505    0.000 {built-in method builtins.len}
              182724750 1011.957    0.000 1011.957    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9236965021  965.917    0.000  965.917    0.000 {method 'values' of 'collections.OrderedDict' objects}
               60908250  932.088    0.000  932.088    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              121816500  822.508    0.000  822.508    0.000 {built-in method broadcast_tensors}
                2436330   90.082    0.000  796.337    0.000 replaybuffer.py:34(save_option_critic)
                2436330  109.373    0.000  775.902    0.000 optimizer.py:189(zero_grad)
               60908250  156.331    0.000  745.882    0.000 utils.py:77(clamp_probs)
              184551996  663.195    0.000  663.195    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               60908250  634.238    0.000  634.238    0.000 {built-in method bernoulli}
               60908250  596.959    0.000  596.959    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               60908250  589.551    0.000  589.551    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               34108614  561.133    0.000  561.133    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               61270025  559.705    0.000  559.705    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               60908250  116.114    0.000  542.938    0.000 layers.py:729(isFree)
              366667664  528.674    0.000  528.674    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              121816500  525.314    0.000  525.314    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               60908250  510.629    0.000  510.629    0.000 {built-in method clamp}
               34108614  509.901    0.000  509.901    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               19490648  305.518    0.000  508.641    0.000 layer.py:167(NoRock_update)
              182724775  138.849    0.000  491.165    0.000 {built-in method builtins.all}
               16445230  484.668    0.000  484.668    0.000 {built-in method tensor}
               11058668  218.846    0.000  472.648    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60908250  443.263    0.000  443.263    0.000 {built-in method log}
              804367564  282.818    0.000  440.714    0.000 {built-in method builtins.isinstance}
               60908250  435.013    0.000  435.013    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              391724848  360.798    0.000  426.824    0.000 layer.py:95(isFree)
              183091421  420.141    0.000  420.141    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               34108600  393.448    0.000  393.448    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60908250  392.356    0.000  392.356    0.000 {built-in method all}
              189424671  382.258    0.000  382.258    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                7308994   18.927    0.000  380.805    0.000 game.py:37(board)


Traceback (most recent call last):
  File "main.py", line 227, in <module>
    
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    enablePrint()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601863: <Diamonds3_option_critic_0> in cluster <dcc> Exited

Job <Diamonds3_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:09 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:10 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:10 2021
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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258285.59 sec.
    Max Memory :                                 905 MB
    Average Memory :                             895.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15479.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258916 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

