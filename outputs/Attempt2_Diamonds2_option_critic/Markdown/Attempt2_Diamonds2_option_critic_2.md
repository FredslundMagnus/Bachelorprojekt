
# Parameters

    Name :                      Attempt2_Diamonds2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal5
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


      49498116932 function calls (47983262340 primitive calls) in 258900.87 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.867 258900.867 {built-in method builtins.exec}
                      1    0.371    0.371 258900.867 258900.867 <string>:1(<module>)
                      1 6030.807 6030.807 258900.496 258900.496 optionCritic.py:195(option_critic_run)
               53871050 9539.237    0.000 111855.467    0.002 optionCritic.py:143(actor_loss_fn)
        2001234063/493383378 10326.908    0.000 110789.663    0.000 module.py:866(_call_impl)
              167538965  848.028    0.000 103434.148    0.001 optionCritic.py:70(get_state)
              167538965 2314.516    0.000 100012.018    0.001 container.py:117(forward)
                2154842   19.345    0.000 75982.669    0.035 tensor.py:195(backward)
                2154842   22.918    0.000 75963.015    0.035 __init__.py:68(backward)
                2154842 75888.346    0.035 75888.346    0.035 {method 'run_backward' of 'torch._C._EngineBase' objects}
              335077930  940.764    0.000 62670.504    0.000 conv.py:398(forward)
              335077930  500.608    0.000 61331.994    0.000 conv.py:390(_conv_forward)
              335077930 60831.386    0.000 60831.386    0.000 {built-in method conv2d}
              660922343 1538.757    0.000 21266.928    0.000 linear.py:93(forward)
               53871050 3265.538    0.000 19209.929    0.000 optionCritic.py:91(get_action)
              660922343  651.326    0.000 19050.013    0.000 functional.py:1737(linear)
              660922343 18260.528    0.000 18260.528    0.000 {built-in method torch._C._nn.linear}
               53871050 1271.439    0.000 14936.497    0.000 optionCritic.py:80(predict_option_termination)
                2154842   51.614    0.000 8615.764    0.004 optimizer.py:84(wrapper)
                2154842   28.188    0.000 8427.628    0.004 grad_mode.py:24(decorate_context)
                2154842  122.943    0.000 8346.107    0.004 rmsprop.py:56(step)
                2154842  129.775    0.000 8082.654    0.004 _functional.py:203(rmsprop)
              107742100 1301.506    0.000 7993.691    0.000 distribution.py:34(__init__)
              502616895  505.515    0.000 7170.223    0.000 activation.py:713(forward)
              502616895  533.513    0.000 6664.708    0.000 functional.py:1364(leaky_relu)
               53871050  544.584    0.000 6418.307    0.000 categorical.py:115(log_prob)
               53871050  520.137    0.000 6351.646    0.000 bernoulli.py:34(__init__)
              502616895 6015.701    0.000 6015.701    0.000 {built-in method torch._C._nn.leaky_relu}
              163692553  373.199    0.000 5431.516    0.000 optionCritic.py:77(get_Q)
               53871050  724.882    0.000 5376.597    0.000 categorical.py:49(__init__)
                 538710   95.766    0.000 4875.513    0.009 optionCritic.py:116(critic_loss_fn)
              108280810  411.731    0.000 4390.373    0.000 optionCritic.py:88(get_terminations)
                2154842   11.852    0.000 4324.501    0.002 game.py:42(step)
                2154842   20.898    0.000 4180.992    0.002 layers.py:827(step)
               30167782 4103.864    0.000 4103.864    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               53871050 2224.318    0.000 3296.561    0.000 constraints.py:398(check)
               30167782 2810.858    0.000 2810.858    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               53871050  457.525    0.000 2639.198    0.000 distribution.py:240(_validate_sample)
               53871050  471.191    0.000 2264.304    0.000 bernoulli.py:86(sample)
                2154842   78.490    0.000 2257.394    0.001 layers.py:17(step)
               53871050 2233.865    0.000 2233.865    0.000 constraints.py:364(check)
               53871050  142.935    0.000 2172.265    0.000 layer.py:106(move)
              167538965  225.980    0.000 2031.771    0.000 activation.py:101(forward)
                2154843  184.345    0.000 1894.708    0.001 layers.py:793(update)
             2593406221 1815.304    0.000 1815.467    0.000 module.py:934(__getattr__)
              167538965  186.528    0.000 1805.792    0.000 functional.py:1195(relu)
              377097350 1798.034    0.000 1798.034    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               53871050  923.823    0.000 1768.229    0.000 categorical.py:123(entropy)
               53871050 1717.964    0.000 1717.964    0.000 constraints.py:249(check)
              167538965  174.929    0.000 1615.186    0.000 flatten.py:39(forward)
              162690570  219.138    0.000 1601.450    0.000 tensor.py:525(__rsub__)
              107742100  578.085    0.000 1597.656    0.000 functional.py:46(broadcast_tensors)
               53871050  399.605    0.000 1592.022    0.000 utils.py:11(broadcast_all)
              167538965 1591.344    0.000 1591.344    0.000 {built-in method relu}
              161613150  214.624    0.000 1579.898    0.000 utils.py:106(__get__)
              167538965 1440.258    0.000 1440.258    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               53871050  318.247    0.000 1430.678    0.000 layers.py:844(check)
               23703262   57.672    0.000 1403.980    0.000 tensor.py:575(__iter__)
              162690570 1354.474    0.000 1354.474    0.000 {built-in method rsub}
               23703262 1312.038    0.000 1312.038    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              108280810 1304.576    0.000 1304.576    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                 538710 1017.841    0.002 1247.290    0.002 replaybuffer.py:42(sample_option_critic)
               53871050  349.222    0.000 1244.015    0.000 categorical.py:108(sample)
              162151860 1228.803    0.000 1228.803    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2024937325 1209.740    0.000 1209.740    0.000 {built-in method torch._C._get_tracing_state}
               53871050   65.759    0.000 1196.258    0.000 categorical.py:88(logits)
             8769023465 1124.875    0.000 1141.254    0.000 {built-in method builtins.len}
               53871050   65.549    0.000 1130.498    0.000 utils.py:82(probs_to_logits)
              161613150 1106.826    0.000 1106.826    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              161613150  986.699    0.000  986.699    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8172475217  944.920    0.000  944.920    0.000 {method 'values' of 'collections.OrderedDict' objects}
              107742100  858.778    0.000  858.778    0.000 {built-in method broadcast_tensors}
               53871050  823.453    0.000  823.453    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2154842   84.310    0.000  739.386    0.000 replaybuffer.py:34(save_option_critic)
                1002007   16.138    0.000  678.538    0.001 layers.py:849(restart)
                2154842  102.993    0.000  664.396    0.000 optimizer.py:189(zero_grad)
               53871050  143.669    0.000  652.619    0.000 utils.py:77(clamp_probs)
              163229280  644.401    0.000  644.401    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               53871050  641.781    0.000  641.781    0.000 {built-in method bernoulli}
                1002007    8.289    0.000  565.811    0.001 level.py:8(__init__)
               53871050  550.017    0.000  550.017    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               54873033  534.614    0.000  534.614    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              324303720  529.640    0.000  529.640    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               19393587  312.688    0.000  516.448    0.000 layer.py:175(NoRock_update)
               53871050  508.950    0.000  508.950    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1002007   20.305    0.000  503.268    0.001 levels.py:249(generate)
               53871050  107.005    0.000  492.250    0.000 layers.py:838(isFree)
              711433066  298.926    0.000  486.688    0.000 {built-in method builtins.isinstance}
                6513573   79.357    0.000  461.865    0.000 level.py:41(notUsed)
              107742100  461.463    0.000  461.463    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               53871050  449.903    0.000  449.903    0.000 {built-in method clamp}
               14545186  426.709    0.000  426.709    0.000 {built-in method tensor}
               30167782  419.374    0.000  419.374    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               53871050  412.330    0.000  412.330    0.000 {built-in method log}
              162619465  408.223    0.000  408.223    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              161613175  138.160    0.000  405.782    0.000 {built-in method builtins.all}
              167538979  396.644    0.000  396.644    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               53871050  389.688    0.000  389.688    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              360851159  319.776    0.000  385.245    0.000 layer.py:103(isFree)
             1194657910  256.568    0.000  379.978    0.000 enum.py:646(__hash__)


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
Subject: Job 9606121: <Attempt2_Diamonds2_option_critic_2> in cluster <dcc> Exited

Job <Attempt2_Diamonds2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:09 2021
Terminated at Thu May  6 01:28:29 2021
Results reported at Thu May  6 01:28:29 2021

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

    CPU time :                                   258287.75 sec.
    Max Memory :                                 1027 MB
    Average Memory :                             1006.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15357.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

