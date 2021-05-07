[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Diamonds1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal2
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


      33904305156 function calls (32852412865 primitive calls) in 258900.81 seconds

##    Ordered by: cumulative time
   List reduced from 427 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.811 258900.811 {built-in method builtins.exec}
                      1    0.309    0.309 258900.811 258900.811 <string>:1(<module>)
                      1 3889.333 3889.333 258900.502 258900.502 optionCritic.py:195(option_critic_run)
               37796225 10177.572    0.000 108468.141    0.003 optionCritic.py:143(actor_loss_fn)
        1396939735/345146401 10080.556    0.000 105655.531    0.000 module.py:866(_call_impl)
              116865926  785.725    0.000 96421.777    0.001 optionCritic.py:70(get_state)
              116865926 2853.930    0.000 93297.806    0.001 container.py:117(forward)
                1511849   12.101    0.000 84423.717    0.056 tensor.py:195(backward)
                1511849   14.072    0.000 84411.321    0.056 __init__.py:68(backward)
                1511849 84357.316    0.056 84357.316    0.056 {method 'run_backward' of 'torch._C._EngineBase' objects}
              233731852  910.597    0.000 54905.029    0.000 conv.py:398(forward)
              233731852  386.547    0.000 53660.942    0.000 conv.py:390(_conv_forward)
              233731852 53274.395    0.000 53274.395    0.000 {built-in method conv2d}
               37796225 3882.922    0.000 23109.121    0.001 optionCritic.py:91(get_action)
              462012327 1619.039    0.000 22021.709    0.000 linear.py:93(forward)
              462012327  594.369    0.000 19781.368    0.000 functional.py:1737(linear)
              462012327 19065.978    0.000 19065.978    0.000 {built-in method torch._C._nn.linear}
               37796225 1218.418    0.000 13441.864    0.000 optionCritic.py:80(predict_option_termination)
               75592450 1125.797    0.000 8593.175    0.000 distribution.py:34(__init__)
              350597778  477.145    0.000 8035.374    0.000 activation.py:713(forward)
               37796225  616.591    0.000 7560.803    0.000 categorical.py:115(log_prob)
              350597778  446.256    0.000 7558.230    0.000 functional.py:1364(leaky_relu)
                1511849   33.974    0.000 7025.288    0.005 optimizer.py:84(wrapper)
              350597778 7024.563    0.000 7024.563    0.000 {built-in method torch._C._nn.leaky_relu}
                1511849   16.787    0.000 6885.164    0.005 grad_mode.py:24(decorate_context)
                1511849  104.950    0.000 6836.270    0.005 rmsprop.py:56(step)
               37796225  891.640    0.000 6808.798    0.000 categorical.py:49(__init__)
                1511849  155.663    0.000 6609.366    0.004 _functional.py:203(rmsprop)
              114740616  459.466    0.000 6436.650    0.000 optionCritic.py:77(get_Q)
               75743634  462.168    0.000 5247.899    0.000 optionCritic.py:88(get_terminations)
               37796225  316.014    0.000 4904.696    0.000 bernoulli.py:34(__init__)
               21165868 4508.328    0.000 4508.328    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37796225 2786.861    0.000 4237.466    0.000 constraints.py:398(check)
               37796225  470.030    0.000 3145.468    0.000 distribution.py:240(_validate_sample)
                1511849   10.613    0.000 3120.878    0.002 game.py:42(step)
                1511849   15.114    0.000 2997.507    0.002 layers.py:827(step)
                 151184   34.464    0.000 2477.177    0.016 optionCritic.py:116(critic_loss_fn)
              116865926  167.799    0.000 2302.788    0.000 activation.py:101(forward)
               37796225 1099.472    0.000 2274.102    0.000 categorical.py:123(entropy)
              116865926  144.523    0.000 2134.988    0.000 functional.py:1195(relu)
               37796225 2119.867    0.000 2119.867    0.000 constraints.py:364(check)
               37796225 2107.067    0.000 2107.067    0.000 constraints.py:249(check)
              116865926 1963.617    0.000 1963.617    0.000 {built-in method relu}
             1413570074 1918.027    0.000 1918.027    0.000 {built-in method torch._C._get_tracing_state}
              113388675  211.880    0.000 1866.951    0.000 utils.py:106(__get__)
               37796225  332.324    0.000 1855.113    0.000 bernoulli.py:86(sample)
              264573575 1793.997    0.000 1793.997    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              113691043  214.421    0.000 1763.987    0.000 tensor.py:525(__rsub__)
             1812231208 1616.688    0.000 1616.692    0.000 module.py:934(__getattr__)
              113388675 1611.129    0.000 1611.129    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              116865926  115.300    0.000 1576.197    0.000 flatten.py:39(forward)
                1511850  158.448    0.000 1541.277    0.001 layers.py:793(update)
              113691043 1514.684    0.000 1514.684    0.000 {built-in method rsub}
               37796225   74.724    0.000 1497.951    0.000 categorical.py:88(logits)
              113539859 1494.122    0.000 1494.122    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              116865926 1460.897    0.000 1460.897    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1511849   62.974    0.000 1434.748    0.001 layers.py:17(step)
               37796225  369.439    0.000 1428.309    0.000 categorical.py:108(sample)
               37796225   77.765    0.000 1423.227    0.000 utils.py:82(probs_to_logits)
               37796225  107.969    0.000 1367.124    0.000 layer.py:106(move)
               75592450  412.884    0.000 1332.766    0.000 functional.py:46(broadcast_tensors)
               75743634 1283.055    0.000 1283.055    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              113388675 1129.804    0.000 1129.804    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               16630339   46.041    0.000 1084.459    0.000 tensor.py:575(__iter__)
             6046626873 1056.646    0.000 1068.921    0.000 {built-in method builtins.len}
               37796225  203.922    0.000 1005.554    0.000 utils.py:11(broadcast_all)
               16630339 1002.467    0.000 1002.467    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               37796225  136.196    0.000  877.363    0.000 utils.py:77(clamp_probs)
             5704624866  852.776    0.000  852.776    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37796225  185.603    0.000  843.055    0.000 layers.py:844(check)
               37796225  824.902    0.000  824.902    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               75592450  788.811    0.000  788.811    0.000 {built-in method broadcast_tensors}
                1511849   80.171    0.000  751.488    0.000 replaybuffer.py:34(save_option_critic)
               37796225  741.168    0.000  741.168    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              113842227  735.140    0.000  735.140    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               21165868  704.014    0.000  704.014    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               37796225  696.328    0.000  696.328    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1049597   17.995    0.000  684.901    0.001 layers.py:849(restart)
              227079718  668.102    0.000  668.102    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37796225  641.395    0.000  641.395    0.000 {built-in method clamp}
               38845798  621.614    0.000  621.614    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37796225  618.954    0.000  618.954    0.000 {built-in method bernoulli}
               75592450  591.148    0.000  591.148    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1049597    8.998    0.000  555.210    0.001 level.py:8(__init__)
                1511849   96.736    0.000  496.328    0.000 optimizer.py:189(zero_grad)
               37796225  482.044    0.000  482.044    0.000 {built-in method all}
                1049597   19.389    0.000  480.658    0.000 levels.py:151(generate)
               37796225  468.099    0.000  468.099    0.000 {built-in method log}
               37796225  465.674    0.000  465.674    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                5036987   70.604    0.000  441.463    0.000 level.py:41(notUsed)
               21165868  431.900    0.000  431.900    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               21165868  431.628    0.000  431.628    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               21165868  377.832    0.000  377.832    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10582950  226.506    0.000  357.114    0.000 layer.py:175(NoRock_update)
               37796225  339.770    0.000  339.770    0.000 {built-in method multinomial}
               37796225   89.004    0.000  336.277    0.000 layers.py:838(isFree)
              497721572  216.390    0.000  325.746    0.000 {built-in method builtins.isinstance}
              116865940  321.057    0.000  321.057    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              114441294  315.003    0.000  315.003    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                9524650  305.720    0.000  305.720    0.000 {built-in method tensor}


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
Subject: Job 9607845: <Attempt3_Diamonds1_option_critic_2> in cluster <dcc> Exited

Job <Attempt3_Diamonds1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:23 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:24 2021
Terminated at Thu May  6 13:26:34 2021
Results reported at Thu May  6 13:26:34 2021

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

    CPU time :                                   258178.72 sec.
    Max Memory :                                 859 MB
    Average Memory :                             843.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15525.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258939 sec.
    Turnaround time :                            258911 sec.

The output (if any) is above this job summary.

