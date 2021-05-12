
# Parameters

    Name :                      Attempt5_Monsters_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.MonsterLevel
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


      49470610747 function calls (47939877496 primitive calls) in 258901.64 seconds

##    Ordered by: cumulative time
   List reduced from 435 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.637 258901.637 {built-in method builtins.exec}
                      1    0.337    0.337 258901.637 258901.637 <string>:1(<module>)
                      1 5391.751 5391.751 258901.300 258901.300 optionCritic.py:195(option_critic_run)
               54914176 9153.932    0.000 112321.961    0.002 optionCritic.py:143(actor_loss_fn)
        2026498664/501343220 10082.493    0.000 109846.808    0.000 module.py:866(_call_impl)
              169461716  772.435    0.000 102143.691    0.001 optionCritic.py:70(get_state)
              169461716 2165.614    0.000 98974.973    0.001 container.py:117(forward)
                1716068   13.314    0.000 81184.033    0.047 tensor.py:195(backward)
                1716068   17.132    0.000 81170.447    0.047 __init__.py:68(backward)
                1716068 81114.454    0.047 81114.454    0.047 {method 'run_backward' of 'torch._C._EngineBase' objects}
              338923432  926.160    0.000 59805.520    0.000 conv.py:398(forward)
              338923432  572.306    0.000 58506.739    0.000 conv.py:390(_conv_forward)
              338923432 57934.433    0.000 57934.433    0.000 {built-in method conv2d}
              670804936 1644.898    0.000 23594.412    0.000 linear.py:93(forward)
              670804936  630.228    0.000 21283.164    0.000 functional.py:1737(linear)
               54914176 3462.948    0.000 20725.795    0.000 optionCritic.py:91(get_action)
              670804936 20497.390    0.000 20497.390    0.000 {built-in method torch._C._nn.linear}
               54914176 1137.977    0.000 13708.308    0.000 optionCritic.py:80(predict_option_termination)
              109828352 1225.138    0.000 8147.709    0.000 distribution.py:34(__init__)
              508385148  532.175    0.000 7054.577    0.000 activation.py:713(forward)
               54914176  573.197    0.000 6917.822    0.000 categorical.py:115(log_prob)
              508385148  526.517    0.000 6522.402    0.000 functional.py:1364(leaky_relu)
              508385148 5879.673    0.000 5879.673    0.000 {built-in method torch._C._nn.leaky_relu}
               54914176  774.605    0.000 5831.489    0.000 categorical.py:49(__init__)
              166709959  382.761    0.000 5588.789    0.000 optionCritic.py:77(get_Q)
               54914176  415.499    0.000 5475.516    0.000 bernoulli.py:34(__init__)
                1716068   10.939    0.000 5373.840    0.003 game.py:42(step)
                1716068   38.928    0.000 5316.140    0.003 optimizer.py:84(wrapper)
                1716068   15.456    0.000 5251.292    0.003 layers.py:827(step)
                1716068   21.335    0.000 5170.708    0.003 grad_mode.py:24(decorate_context)
                1716068  119.587    0.000 5110.723    0.003 adam.py:55(step)
                1716068  605.628    0.000 4858.662    0.003 _functional.py:53(adam)
              110257369  393.380    0.000 4319.216    0.000 optionCritic.py:88(get_terminations)
                 429017   70.113    0.000 3635.403    0.008 optionCritic.py:116(critic_loss_fn)
               54914176 2400.485    0.000 3556.634    0.000 constraints.py:398(check)
                1716068   88.308    0.000 2897.491    0.002 layers.py:17(step)
               54914176  492.605    0.000 2822.225    0.000 distribution.py:240(_validate_sample)
               54914176  230.640    0.000 2800.930    0.000 layer.py:106(move)
                1716069  170.049    0.000 2330.388    0.001 layers.py:793(update)
               54914176 2161.121    0.000 2161.121    0.000 constraints.py:364(check)
              169461716  217.020    0.000 2018.992    0.000 activation.py:101(forward)
               54914176  261.529    0.000 1950.109    0.000 layers.py:844(check)
               54914176  369.284    0.000 1931.053    0.000 bernoulli.py:86(sample)
               54914176 1000.631    0.000 1915.665    0.000 categorical.py:123(entropy)
               54914176 1821.217    0.000 1821.217    0.000 constraints.py:249(check)
              169461716  185.009    0.000 1801.972    0.000 functional.py:1195(relu)
             2630851461 1776.821    0.000 1776.955    0.000 module.py:934(__getattr__)
              164742528  238.203    0.000 1737.086    0.000 utils.py:106(__get__)
              384399232 1657.367    0.000 1657.367    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              169461716  159.721    0.000 1599.762    0.000 flatten.py:39(forward)
              169461716 1586.879    0.000 1586.879    0.000 {built-in method relu}
              165600562  185.369    0.000 1543.768    0.000 tensor.py:525(__rsub__)
              109828352  513.145    0.000 1459.544    0.000 functional.py:46(broadcast_tensors)
              169461716 1440.040    0.000 1440.040    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               54914176  373.544    0.000 1366.899    0.000 categorical.py:108(sample)
               18876748   45.718    0.000 1343.840    0.000 tensor.py:575(__iter__)
              165600562 1326.903    0.000 1326.903    0.000 {built-in method rsub}
               54914176   67.486    0.000 1313.545    0.000 categorical.py:88(logits)
               18876748 1269.866    0.000 1269.866    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               54914176   71.722    0.000 1246.059    0.000 utils.py:82(probs_to_logits)
             2045375412 1235.551    0.000 1235.551    0.000 {built-in method torch._C._get_tracing_state}
              110257369 1230.421    0.000 1230.421    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              165171545 1211.941    0.000 1211.941    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              164742528 1196.452    0.000 1196.452    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8658855519 1177.052    0.000 1190.392    0.000 {built-in method builtins.len}
               54914176  231.835    0.000 1172.293    0.000 utils.py:11(broadcast_all)
               48049892 1138.636    0.000 1138.636    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54914176  638.894    0.000 1129.630    0.000 layers.py:538(check)
              164742528 1031.316    0.000 1031.316    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8275456372  999.979    0.000  999.979    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1109428   17.209    0.000  947.340    0.001 layers.py:849(restart)
                 429017  724.355    0.002  891.655    0.002 replaybuffer.py:42(sample_option_critic)
               54914176  884.311    0.000  884.311    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1109428    8.470    0.000  807.786    0.001 level.py:8(__init__)
              109828352  799.405    0.000  799.405    0.000 {built-in method broadcast_tensors}
               54914176  149.083    0.000  742.680    0.000 utils.py:77(clamp_probs)
                1109428  117.859    0.000  731.617    0.001 levels.py:428(generate)
                1716068   82.244    0.000  724.822    0.000 replaybuffer.py:34(save_option_critic)
               24024946  718.867    0.000  718.867    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               24024946  648.658    0.000  648.658    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              166029579  641.347    0.000  641.347    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               24024946  614.848    0.000  614.848    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               54914176  593.598    0.000  593.598    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               54914176  591.478    0.000  591.478    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               54914176  587.936    0.000  587.936    0.000 {built-in method bernoulli}
               48049892  585.457    0.000  585.457    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10296414  391.840    0.000  567.799    0.000 layer.py:159(update)
               56023573  539.317    0.000  539.317    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               24024946  537.144    0.000  537.144    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54801771   59.626    0.000  536.105    0.000 {built-in method builtins.any}
              330343090  531.158    0.000  531.158    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              109828352  508.197    0.000  508.197    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1716068   83.661    0.000  494.143    0.000 optimizer.py:189(zero_grad)
                5547140   79.416    0.000  492.326    0.000 level.py:41(notUsed)
               54914176  481.910    0.000  481.910    0.000 {built-in method clamp}
              382615406  155.980    0.000  476.653    0.000 layers.py:809(<genexpr>)
               54914176   98.321    0.000  474.083    0.000 layers.py:838(isFree)
               54914176  431.656    0.000  431.656    0.000 {built-in method log}
               54914176  422.802    0.000  422.802    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              733825890  274.977    0.000  403.114    0.000 {built-in method builtins.isinstance}


Traceback (most recent call last):
  File "main.py", line 268, in <module>
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
Subject: Job 9618619: <Attempt5_Monsters_option_critic_0> in cluster <dcc> Exited

Job <Attempt5_Monsters_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:28 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sat May  8 23:13:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:13:45 2021
Terminated at Tue May 11 23:09:03 2021
Results reported at Tue May 11 23:09:03 2021

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

    CPU time :                                   258267.81 sec.
    Max Memory :                                 786 MB
    Average Memory :                             762.94 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15598.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259024 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.

