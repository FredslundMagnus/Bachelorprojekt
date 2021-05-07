
# Parameters

    Name :                      Attempt2_Diamonds4_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal7
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


      49081311623 function calls (47610112963 primitive calls) in 258900.63 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.629 258900.629 {built-in method builtins.exec}
                      1    0.346    0.346 258900.629 258900.629 <string>:1(<module>)
                      1 5736.763 5736.763 258900.283 258900.283 optionCritic.py:195(option_critic_run)
               52318575 9514.395    0.000 112779.950    0.002 optionCritic.py:143(actor_loss_fn)
        1942784664/478387761 10114.755    0.000 111804.941    0.000 module.py:866(_call_impl)
              162710767  831.095    0.000 104442.120    0.001 optionCritic.py:70(get_state)
              162710767 2249.978    0.000 101076.286    0.001 container.py:117(forward)
                2092743   16.468    0.000 74970.992    0.036 tensor.py:195(backward)
                2092743   19.797    0.000 74954.240    0.036 __init__.py:68(backward)
                2092743 74884.915    0.036 74884.915    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              325421534  943.134    0.000 64028.062    0.000 conv.py:398(forward)
              325421534  545.618    0.000 62678.277    0.000 conv.py:390(_conv_forward)
              325421534 62132.659    0.000 62132.659    0.000 {built-in method conv2d}
              641098528 1520.594    0.000 21361.335    0.000 linear.py:93(forward)
              641098528  652.927    0.000 19117.232    0.000 functional.py:1737(linear)
               52318575 3132.762    0.000 18516.883    0.000 optionCritic.py:91(get_action)
              641098528 18321.860    0.000 18321.860    0.000 {built-in method torch._C._nn.linear}
               52318575 1258.333    0.000 15045.648    0.000 optionCritic.py:80(predict_option_termination)
                2092743   44.266    0.000 8632.407    0.004 optimizer.py:84(wrapper)
                2092743   25.263    0.000 8461.423    0.004 grad_mode.py:24(decorate_context)
                2092743  115.122    0.000 8389.453    0.004 rmsprop.py:56(step)
                2092743  125.545    0.000 8142.852    0.004 _functional.py:203(rmsprop)
              104637150 1309.763    0.000 7920.080    0.000 distribution.py:34(__init__)
              488132301  521.939    0.000 7145.338    0.000 activation.py:713(forward)
              488132301  556.826    0.000 6623.398    0.000 functional.py:1364(leaky_relu)
               52318575  556.124    0.000 6499.966    0.000 bernoulli.py:34(__init__)
               52318575  547.127    0.000 6221.812    0.000 categorical.py:115(log_prob)
              488132301 5965.098    0.000 5965.098    0.000 {built-in method torch._C._nn.leaky_relu}
              158198084  369.883    0.000 5404.715    0.000 optionCritic.py:77(get_Q)
                2092743   12.544    0.000 5370.488    0.003 game.py:42(step)
                2092743   18.170    0.000 5207.663    0.002 layers.py:827(step)
               52318575  698.385    0.000 5157.948    0.000 categorical.py:49(__init__)
                 523185   90.926    0.000 4959.288    0.009 optionCritic.py:116(critic_loss_fn)
              105160335  418.538    0.000 4343.277    0.000 optionCritic.py:88(get_terminations)
               29298396 4267.423    0.000 4267.423    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2092743   82.089    0.000 3868.425    0.002 layers.py:17(step)
               52318575  257.746    0.000 3779.938    0.000 layer.py:106(move)
               52318575 2115.576    0.000 3146.865    0.000 constraints.py:398(check)
               29298396 2832.174    0.000 2832.174    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52318575  402.136    0.000 2627.778    0.000 layers.py:844(check)
               52318575  443.779    0.000 2532.238    0.000 distribution.py:240(_validate_sample)
               52318575 2305.361    0.000 2305.361    0.000 constraints.py:364(check)
               52318575  481.369    0.000 2246.953    0.000 bernoulli.py:86(sample)
              366230025 2022.829    0.000 2022.829    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              162710767  219.101    0.000 1979.034    0.000 activation.py:101(forward)
             2516337146 1846.114    0.000 1846.271    0.000 module.py:934(__getattr__)
              162710767  192.256    0.000 1759.932    0.000 functional.py:1195(relu)
               52318575  897.337    0.000 1713.595    0.000 categorical.py:123(entropy)
               52318575 1639.450    0.000 1639.450    0.000 constraints.py:249(check)
              162710767  199.670    0.000 1633.460    0.000 flatten.py:39(forward)
              158002095  216.542    0.000 1613.689    0.000 tensor.py:525(__rsub__)
              104637150  566.731    0.000 1590.068    0.000 functional.py:46(broadcast_tensors)
               52318575  378.737    0.000 1581.268    0.000 utils.py:11(broadcast_all)
              156955725  219.161    0.000 1546.501    0.000 utils.py:106(__get__)
              162710767 1541.212    0.000 1541.212    0.000 {built-in method relu}
              162710767 1433.791    0.000 1433.791    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              158002095 1368.380    0.000 1368.380    0.000 {built-in method rsub}
               23020173   54.870    0.000 1335.465    0.000 tensor.py:575(__iter__)
              105160335 1321.100    0.000 1321.100    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                2092744  176.494    0.000 1313.658    0.001 layers.py:793(update)
               23020173 1247.232    0.000 1247.232    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              157478910 1214.523    0.000 1214.523    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               52318575  335.242    0.000 1212.196    0.000 categorical.py:108(sample)
             1965804837 1181.513    0.000 1181.513    0.000 {built-in method torch._C._get_tracing_state}
               52318575   63.364    0.000 1168.279    0.000 categorical.py:88(logits)
               52318575   62.263    0.000 1104.915    0.000 utils.py:82(probs_to_logits)
             8633439967 1081.651    0.000 1099.080    0.000 {built-in method builtins.len}
                 523185  868.334    0.002 1092.006    0.002 replaybuffer.py:42(sample_option_critic)
              156955725 1072.547    0.000 1072.547    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              156955725  970.161    0.000  970.161    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7933849423  916.667    0.000  916.667    0.000 {method 'values' of 'collections.OrderedDict' objects}
              104637150  852.711    0.000  852.711    0.000 {built-in method broadcast_tensors}
               52318575  772.516    0.000  772.516    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               52318575  133.509    0.000  737.498    0.000 layers.py:838(isFree)
                2092743   80.397    0.000  699.013    0.000 replaybuffer.py:34(save_option_critic)
               52318575  650.883    0.000  650.883    0.000 {built-in method bernoulli}
               52318575  139.792    0.000  644.244    0.000 utils.py:77(clamp_probs)
              158525280  636.174    0.000  636.174    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
              451751044  500.429    0.000  603.989    0.000 layer.py:103(isFree)
                2092743  100.121    0.000  594.097    0.000 optimizer.py:189(zero_grad)
               23020184  348.506    0.000  585.304    0.000 layer.py:159(update)
               52318575  421.622    0.000  571.276    0.000 layers.py:471(check)
               52318575  541.998    0.000  541.998    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              314957820  528.522    0.000  528.522    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               52514564  518.706    0.000  518.706    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              690930836  306.296    0.000  508.431    0.000 {built-in method builtins.isinstance}
               52318575  504.452    0.000  504.452    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              104637150  452.962    0.000  452.962    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
             1389976207  312.693    0.000  450.366    0.000 enum.py:646(__hash__)
               14126017  440.210    0.000  440.210    0.000 {built-in method tensor}
               52318575  434.206    0.000  434.206    0.000 {built-in method clamp}
              157155922  412.919    0.000  412.919    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               52318575  398.409    0.000  398.409    0.000 {built-in method log}
              162710781  388.810    0.000  388.810    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               52318575  233.944    0.000  383.396    0.000 layers.py:246(check)
               52318575  373.473    0.000  373.473    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               29298396  362.394    0.000  362.394    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52318575  252.090    0.000  352.414    0.000 layers.py:77(check)
               54411344  186.629    0.000  345.623    0.000 grad_mode.py:119(__enter__)
                6278233   13.684    0.000  343.928    0.000 game.py:38(board)


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
Subject: Job 9606126: <Attempt2_Diamonds4_option_critic_1> in cluster <dcc> Exited

Job <Attempt2_Diamonds4_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:11 2021
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

    CPU time :                                   258214.94 sec.
    Max Memory :                                 874 MB
    Average Memory :                             860.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15510.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258948 sec.
    Turnaround time :                            258923 sec.

The output (if any) is above this job summary.

