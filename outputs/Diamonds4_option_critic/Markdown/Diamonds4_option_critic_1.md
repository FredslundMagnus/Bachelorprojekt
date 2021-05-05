
# Parameters

    Name :                      Diamonds4_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal7
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


      54428940110 function calls (52726031930 primitive calls) in 258900.50 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.497 258900.497 {built-in method builtins.exec}
                      1    0.365    0.365 258900.497 258900.497 <string>:1(<module>)
                      1 6228.173 6228.173 258900.132 258900.132 optionCritic.py:195(option_critic_run)
               60558600 9343.905    0.000 112548.753    0.002 optionCritic.py:143(actor_loss_fn)
        2250281955/555246732 10154.287    0.000 111783.997    0.000 module.py:866(_call_impl)
              188337247  858.735    0.000 104047.326    0.001 optionCritic.py:70(get_state)
              188337247 2287.110    0.000 100605.024    0.001 container.py:117(forward)
                2422344   18.343    0.000 74815.905    0.031 tensor.py:195(backward)
                2422344   24.685    0.000 74797.239    0.031 __init__.py:68(backward)
                2422344 74717.299    0.031 74717.299    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              376674494  969.506    0.000 63053.078    0.000 conv.py:398(forward)
              376674494  542.489    0.000 61690.346    0.000 conv.py:390(_conv_forward)
              376674494 61147.856    0.000 61147.856    0.000 {built-in method conv2d}
               60558600 3673.094    0.000 21491.799    0.000 optionCritic.py:91(get_action)
              743583979 1688.128    0.000 21405.668    0.000 linear.py:93(forward)
              743583979  654.902    0.000 19042.082    0.000 functional.py:1737(linear)
              743583979 18236.374    0.000 18236.374    0.000 {built-in method torch._C._nn.linear}
               60558600 1251.068    0.000 14628.056    0.000 optionCritic.py:80(predict_option_termination)
              121117200 1286.065    0.000 8278.770    0.000 distribution.py:34(__init__)
              565011741  530.030    0.000 7486.593    0.000 activation.py:713(forward)
               60558600  598.316    0.000 7156.018    0.000 categorical.py:115(log_prob)
              565011741  565.979    0.000 6956.563    0.000 functional.py:1364(leaky_relu)
              565011741 6280.571    0.000 6280.571    0.000 {built-in method torch._C._nn.leaky_relu}
               60558600  809.144    0.000 6028.860    0.000 categorical.py:49(__init__)
                2422344   55.131    0.000 5983.250    0.002 optimizer.py:84(wrapper)
              184628099  408.605    0.000 5805.966    0.000 optionCritic.py:77(get_Q)
                2422344   30.048    0.000 5785.040    0.002 grad_mode.py:24(decorate_context)
               60558600  459.596    0.000 5734.333    0.000 bernoulli.py:34(__init__)
                2422344  138.888    0.000 5700.636    0.002 rmsprop.py:56(step)
                2422344  135.972    0.000 5409.417    0.002 _functional.py:203(rmsprop)
                 605586   99.189    0.000 4833.306    0.008 optionCritic.py:116(critic_loss_fn)
              121722786  427.045    0.000 4459.976    0.000 optionCritic.py:88(get_terminations)
                2422344   12.046    0.000 4238.347    0.002 game.py:41(step)
                2422344   24.596    0.000 4093.801    0.002 layers.py:718(step)
               60558600 2484.792    0.000 3673.856    0.000 constraints.py:398(check)
               60558600  497.295    0.000 2918.223    0.000 distribution.py:240(_validate_sample)
               33912810 2241.223    0.000 2241.223    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60558600  474.580    0.000 2223.441    0.000 bernoulli.py:86(sample)
              188337247  246.916    0.000 2132.943    0.000 activation.py:101(forward)
               60558600 2130.020    0.000 2130.020    0.000 constraints.py:364(check)
                2422344   89.323    0.000 2041.772    0.001 layers.py:17(step)
                2422345  204.452    0.000 2018.473    0.001 layers.py:684(update)
               60558600 1026.188    0.000 1972.400    0.000 categorical.py:123(entropy)
               60558600  147.651    0.000 1944.192    0.000 layer.py:98(move)
               60558600 1898.403    0.000 1898.403    0.000 constraints.py:249(check)
              188337247  211.758    0.000 1886.026    0.000 functional.py:1195(relu)
             2917195837 1853.859    0.000 1854.036    0.000 module.py:934(__getattr__)
              181675800  236.649    0.000 1768.502    0.000 utils.py:106(__get__)
              423910200 1739.367    0.000 1739.367    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              188337247  171.069    0.000 1687.572    0.000 flatten.py:39(forward)
               33912810 1668.047    0.000 1668.047    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              188337247 1642.659    0.000 1642.659    0.000 {built-in method relu}
              182886972  208.852    0.000 1587.007    0.000 tensor.py:525(__rsub__)
              121117200  573.835    0.000 1576.505    0.000 functional.py:46(broadcast_tensors)
              188337247 1516.503    0.000 1516.503    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 605586 1265.415    0.002 1511.527    0.002 replaybuffer.py:42(sample_option_critic)
               26645784   64.121    0.000 1503.614    0.000 tensor.py:575(__iter__)
               60558600  393.452    0.000 1406.181    0.000 categorical.py:108(sample)
               26645784 1401.570    0.000 1401.570    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              182886972 1349.800    0.000 1349.800    0.000 {built-in method rsub}
               60558600   71.786    0.000 1344.626    0.000 categorical.py:88(logits)
               60558600  297.282    0.000 1320.430    0.000 utils.py:11(broadcast_all)
             2276927739 1308.503    0.000 1308.503    0.000 {built-in method torch._C._get_tracing_state}
               60558600   81.170    0.000 1272.840    0.000 utils.py:82(probs_to_logits)
              182281386 1256.409    0.000 1256.409    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              121722786 1255.938    0.000 1255.938    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              181675800 1249.199    0.000 1249.199    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9736792089 1186.832    0.000 1204.491    0.000 {built-in method builtins.len}
               60558600  249.104    0.000 1161.318    0.000 layers.py:735(check)
              181675800 1028.125    0.000 1028.125    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9189465067  966.109    0.000  966.109    0.000 {method 'values' of 'collections.OrderedDict' objects}
               60558600  915.203    0.000  915.203    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1741152   23.636    0.000  850.309    0.000 layers.py:740(restart)
              121117200  841.672    0.000  841.672    0.000 {built-in method broadcast_tensors}
                2422344   88.401    0.000  792.958    0.000 replaybuffer.py:34(save_option_critic)
                2422344  112.329    0.000  758.250    0.000 optimizer.py:189(zero_grad)
               60558600  156.357    0.000  744.306    0.000 utils.py:77(clamp_probs)
                1741152   12.639    0.000  672.284    0.000 level.py:8(__init__)
               13897741  312.809    0.000  659.379    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60558600  650.274    0.000  650.274    0.000 {built-in method bernoulli}
              183492558  649.756    0.000  649.756    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               60558600  617.382    0.000  617.382    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               60558600  587.949    0.000  587.949    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               62299727  585.243    0.000  585.243    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1741152   27.029    0.000  579.816    0.000 levels.py:441(generate)
               33912810  570.456    0.000  570.456    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              364562772  543.050    0.000  543.050    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                8356142   98.832    0.000  523.778    0.000 level.py:41(notUsed)
              121117200  522.005    0.000  522.005    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               60558600  113.692    0.000  520.400    0.000 layers.py:729(isFree)
               33912810  512.198    0.000  512.198    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               60558600  503.360    0.000  503.360    0.000 {built-in method clamp}
               16956415  298.702    0.000  483.470    0.000 layer.py:167(NoRock_update)
               16350826  455.360    0.000  455.360    0.000 {built-in method tensor}
               60558600  447.364    0.000  447.364    0.000 {built-in method log}
              799749949  287.034    0.000  436.145    0.000 {built-in method builtins.isinstance}
               60558600  432.036    0.000  432.036    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              183421795  419.993    0.000  419.993    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              399184887  336.656    0.000  406.708    0.000 layer.py:95(isFree)
               60558600  398.019    0.000  398.019    0.000 {built-in method all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601867: <Diamonds4_option_critic_1> in cluster <dcc> Done

Job <Diamonds4_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:11 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:13 2021
Terminated at Sun May  2 21:36:16 2021
Results reported at Sun May  2 21:36:16 2021

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

    CPU time :                                   258285.91 sec.
    Max Memory :                                 872 MB
    Average Memory :                             855.14 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15512.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258918 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

