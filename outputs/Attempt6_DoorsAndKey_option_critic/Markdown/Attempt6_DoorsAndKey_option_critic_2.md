
# Parameters

    Name :                      Attempt6_DoorsAndKey_option_critic-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      15397235824 function calls (14881914504 primitive calls) in 258901.11 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.107 258901.107 {built-in method builtins.exec}
                      1    0.347    0.347 258901.107 258901.107 <string>:1(<module>)
                      1 1971.109 1971.109 258900.760 258900.760 optionCritic.py:195(option_critic_run)
                 577714    4.490    0.000 192566.869    0.333 tensor.py:195(backward)
                 577714    6.096    0.000 192562.301    0.333 __init__.py:68(backward)
                 577714 192542.796    0.333 192542.796    0.333 {method 'run_backward' of 'torch._C._EngineBase' objects}
        681934272/168490959 3204.665    0.000 42704.826    0.000 module.py:866(_call_impl)
               18486848 2760.745    0.000 40460.823    0.002 optionCritic.py:143(actor_loss_fn)
               57049257  273.045    0.000 40266.852    0.001 optionCritic.py:70(get_state)
               57049257  757.294    0.000 39185.972    0.001 container.py:117(forward)
              114098514  297.785    0.000 24123.913    0.000 conv.py:398(forward)
              114098514  162.529    0.000 23702.880    0.000 conv.py:390(_conv_forward)
              114098514 23540.351    0.000 23540.351    0.000 {built-in method conv2d}
              225540216  532.496    0.000 9957.244    0.000 linear.py:93(forward)
              225540216  208.684    0.000 9202.237    0.000 functional.py:1737(linear)
              225540216 8942.390    0.000 8942.390    0.000 {built-in method torch._C._nn.linear}
               18486848 1088.588    0.000 6496.261    0.000 optionCritic.py:91(get_action)
               18486848  401.829    0.000 4656.048    0.000 optionCritic.py:80(predict_option_termination)
                 577714   13.385    0.000 3999.006    0.007 optimizer.py:84(wrapper)
                 577714    7.524    0.000 3948.835    0.007 grad_mode.py:24(decorate_context)
                 577714   36.184    0.000 3927.757    0.007 adam.py:55(step)
                 577714  225.812    0.000 3852.893    0.007 _functional.py:53(adam)
               36973696  409.859    0.000 2603.932    0.000 distribution.py:34(__init__)
              171147771  175.783    0.000 2356.061    0.000 activation.py:713(forward)
                 144428   24.659    0.000 2271.771    0.016 optionCritic.py:116(critic_loss_fn)
              171147771  172.962    0.000 2180.278    0.000 functional.py:1364(leaky_relu)
               18486848  178.561    0.000 2160.162    0.000 categorical.py:115(log_prob)
              171147771 1972.348    0.000 1972.348    0.000 {built-in method torch._C._nn.leaky_relu}
               18486848  148.774    0.000 1873.899    0.000 bernoulli.py:34(__init__)
               18486848  250.047    0.000 1828.424    0.000 categorical.py:49(__init__)
               55836730  125.269    0.000 1778.581    0.000 optionCritic.py:77(get_Q)
               37118124  134.652    0.000 1444.754    0.000 optionCritic.py:88(get_terminations)
               18486848  748.775    0.000 1110.259    0.000 constraints.py:398(check)
                 577714    2.980    0.000  908.770    0.002 game.py:42(step)
               18486848  149.256    0.000  881.206    0.000 distribution.py:240(_validate_sample)
                 577714    5.560    0.000  871.541    0.002 layers.py:827(step)
               16175980  843.366    0.000  843.366    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                8087990  758.373    0.000  758.373    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18486848  139.951    0.000  699.822    0.000 bernoulli.py:86(sample)
               18486848  694.118    0.000  694.118    0.000 constraints.py:364(check)
               57049257   76.239    0.000  681.831    0.000 activation.py:101(forward)
                8087990  661.710    0.000  661.710    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               57049257   65.669    0.000  605.593    0.000 functional.py:1195(relu)
               18486848  311.168    0.000  599.455    0.000 categorical.py:123(entropy)
              884817276  598.000    0.000  598.043    0.000 module.py:934(__getattr__)
               18486848  576.368    0.000  576.368    0.000 constraints.py:249(check)
              129407936  567.286    0.000  567.286    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               55460544   72.834    0.000  539.315    0.000 utils.py:106(__get__)
               57049257  530.332    0.000  530.332    0.000 {built-in method relu}
               57049257   54.354    0.000  530.326    0.000 flatten.py:39(forward)
               55749400   65.899    0.000  519.259    0.000 tensor.py:525(__rsub__)
                 577714   26.098    0.000  502.922    0.001 layers.py:17(step)
               36973696  175.506    0.000  486.571    0.000 functional.py:46(broadcast_tensors)
               57049257  475.972    0.000  475.972    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               18486848   46.213    0.000  474.539    0.000 layer.py:106(move)
                8087990  466.009    0.000  466.009    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16175980  449.918    0.000  449.918    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8087990  444.322    0.000  444.322    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               55749400  443.805    0.000  443.805    0.000 {built-in method rsub}
                6354854   15.419    0.000  434.184    0.000 tensor.py:575(__iter__)
               18486848   96.236    0.000  427.065    0.000 utils.py:11(broadcast_all)
               18486848  115.640    0.000  421.548    0.000 categorical.py:108(sample)
               37118124  417.436    0.000  417.436    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                6354854  409.794    0.000  409.794    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               18486848   21.710    0.000  406.991    0.000 categorical.py:88(logits)
               55604972  406.521    0.000  406.521    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              688289126  387.334    0.000  387.334    0.000 {built-in method torch._C._get_tracing_state}
               18486848   22.509    0.000  385.281    0.000 utils.py:82(probs_to_logits)
               55460544  378.741    0.000  378.741    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             2927303326  360.546    0.000  364.897    0.000 {built-in method builtins.len}
                 577715   53.524    0.000  360.330    0.001 layers.py:793(update)
               55460544  329.841    0.000  329.841    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                 144428  267.591    0.002  324.106    0.002 replaybuffer.py:42(sample_option_critic)
             2784786345  307.915    0.000  307.915    0.000 {method 'values' of 'collections.OrderedDict' objects}
               18486848  290.067    0.000  290.067    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               36973696  259.372    0.000  259.372    0.000 {built-in method broadcast_tensors}
                 577714   26.914    0.000  238.469    0.000 replaybuffer.py:34(save_option_critic)
               18486848   44.845    0.000  226.576    0.000 utils.py:77(clamp_probs)
               18486848   68.060    0.000  220.717    0.000 layers.py:844(check)
               18486848  205.304    0.000  205.304    0.000 {built-in method bernoulli}
               55893828  204.814    0.000  204.814    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               18486848  184.656    0.000  184.656    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               18486848  181.731    0.000  181.731    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              111209944  170.796    0.000  170.796    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               18574178  169.011    0.000  169.011    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               18486848   36.178    0.000  167.817    0.000 layers.py:838(isFree)
                 577714   26.264    0.000  164.436    0.000 optimizer.py:189(zero_grad)
               36973696  157.092    0.000  157.092    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               18486848  152.380    0.000  152.380    0.000 {built-in method clamp}
              243308100   94.687    0.000  143.754    0.000 {built-in method builtins.isinstance}
               55549059  136.205    0.000  136.205    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               18486848  136.195    0.000  136.195    0.000 {built-in method log}
               18486848  132.043    0.000  132.043    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              106640802  110.597    0.000  131.639    0.000 layer.py:103(isFree)
                3899572  124.470    0.000  124.470    0.000 {built-in method tensor}
               55460576   39.035    0.000  123.009    0.000 {built-in method builtins.all}
               18486848  120.831    0.000  120.831    0.000 {built-in method all}
               57049271  119.123    0.000  119.123    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                3466290   70.283    0.000  116.549    0.000 layer.py:175(NoRock_update)
               19064588   55.187    0.000  111.418    0.000 grad_mode.py:119(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624176: <Attempt6_DoorsAndKey_option_critic_2> in cluster <dcc> Done

Job <Attempt6_DoorsAndKey_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:30 2021
Job was executed on host(s) <n-62-11-63>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:32 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:32 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

    CPU time :                                   258286.70 sec.
    Max Memory :                                 794 MB
    Average Memory :                             787.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15590.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

