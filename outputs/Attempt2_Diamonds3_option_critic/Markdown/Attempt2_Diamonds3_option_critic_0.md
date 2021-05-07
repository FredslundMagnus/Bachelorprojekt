
# Parameters

    Name :                      Attempt2_Diamonds3_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      49391492823 function calls (47837283533 primitive calls) in 258900.81 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.806 258900.806 {built-in method builtins.exec}
                      1    0.369    0.369 258900.806 258900.806 <string>:1(<module>)
                      1 6230.551 6230.551 258900.437 258900.437 optionCritic.py:195(option_critic_run)
               55270575 10028.953    0.000 116142.570    0.002 optionCritic.py:143(actor_loss_fn)
        2052657107/505633724 10220.148    0.000 114472.791    0.000 module.py:866(_call_impl)
              171891487  881.976    0.000 106686.953    0.001 optionCritic.py:70(get_state)
              171891487 2319.349    0.000 103238.111    0.001 container.py:117(forward)
                2210823   19.782    0.000 70133.056    0.032 tensor.py:195(backward)
                2210823   24.063    0.000 70112.954    0.032 __init__.py:68(backward)
                2210823 70033.631    0.032 70033.631    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              343782974  964.378    0.000 64217.915    0.000 conv.py:398(forward)
              343782974  532.527    0.000 62816.480    0.000 conv.py:390(_conv_forward)
              343782974 62283.954    0.000 62283.954    0.000 {built-in method conv2d}
              677525211 1619.356    0.000 22865.823    0.000 linear.py:93(forward)
              677525211  670.340    0.000 20523.897    0.000 functional.py:1737(linear)
               55270575 3461.719    0.000 20179.658    0.000 optionCritic.py:91(get_action)
              677525211 19704.634    0.000 19704.634    0.000 {built-in method torch._C._nn.linear}
               55270575 1339.334    0.000 15465.475    0.000 optionCritic.py:80(predict_option_termination)
                2210823   52.599    0.000 8529.165    0.004 optimizer.py:84(wrapper)
                2210823   30.224    0.000 8335.368    0.004 grad_mode.py:24(decorate_context)
              110541150 1370.111    0.000 8283.840    0.000 distribution.py:34(__init__)
                2210823  129.040    0.000 8251.601    0.004 rmsprop.py:56(step)
                2210823  137.914    0.000 7978.561    0.004 _functional.py:203(rmsprop)
              515674461  536.802    0.000 7559.919    0.000 activation.py:713(forward)
              515674461  566.810    0.000 7023.116    0.000 functional.py:1364(leaky_relu)
               55270575  566.546    0.000 6683.108    0.000 categorical.py:115(log_prob)
               55270575  553.676    0.000 6493.628    0.000 bernoulli.py:34(__init__)
              515674461 6334.969    0.000 6334.969    0.000 {built-in method torch._C._nn.leaky_relu}
              167377807  380.416    0.000 5675.683    0.000 optionCritic.py:77(get_Q)
               55270575  771.771    0.000 5650.277    0.000 categorical.py:49(__init__)
                 552705  100.783    0.000 4892.620    0.009 optionCritic.py:116(critic_loss_fn)
              111093855  424.090    0.000 4598.378    0.000 optionCritic.py:88(get_terminations)
               30951516 4005.331    0.000 4005.331    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2210823   11.876    0.000 3930.849    0.002 game.py:42(step)
                2210823   22.647    0.000 3784.322    0.002 layers.py:827(step)
               55270575 2318.495    0.000 3446.270    0.000 constraints.py:398(check)
               30951516 2760.285    0.000 2760.285    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               55270575  468.082    0.000 2724.119    0.000 distribution.py:240(_validate_sample)
               55270575  502.330    0.000 2299.279    0.000 bernoulli.py:86(sample)
               55270575 2255.990    0.000 2255.990    0.000 constraints.py:364(check)
                2210823   81.080    0.000 2155.873    0.001 layers.py:17(step)
              171891487  232.854    0.000 2137.009    0.000 activation.py:101(forward)
               55270575  141.308    0.000 2067.710    0.000 layer.py:106(move)
              386894025 1947.627    0.000 1947.627    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              171891487  192.170    0.000 1904.155    0.000 functional.py:1195(relu)
             2659078721 1888.950    0.000 1889.115    0.000 module.py:934(__getattr__)
               55270575  991.806    0.000 1879.899    0.000 categorical.py:123(entropy)
               55270575 1777.509    0.000 1777.509    0.000 constraints.py:249(check)
              171891487 1681.739    0.000 1681.739    0.000 {built-in method relu}
              171891487  166.906    0.000 1662.348    0.000 flatten.py:39(forward)
              166917135  218.437    0.000 1654.303    0.000 tensor.py:525(__rsub__)
              110541150  587.887    0.000 1652.748    0.000 functional.py:46(broadcast_tensors)
              165811725  222.748    0.000 1649.972    0.000 utils.py:106(__get__)
                2210824  189.513    0.000 1597.506    0.001 layers.py:793(update)
               55270575  367.638    0.000 1595.117    0.000 utils.py:11(broadcast_all)
              171891487 1495.442    0.000 1495.442    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               24319053   57.798    0.000 1426.070    0.000 tensor.py:575(__iter__)
              166917135 1406.469    0.000 1406.469    0.000 {built-in method rsub}
              111093855 1371.887    0.000 1371.887    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               24319053 1333.884    0.000 1333.884    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               55270575  271.648    0.000 1323.284    0.000 layers.py:844(check)
              166364430 1309.922    0.000 1309.922    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               55270575  369.427    0.000 1307.621    0.000 categorical.py:108(sample)
                 552705 1066.824    0.002 1295.165    0.002 replaybuffer.py:42(sample_option_critic)
               55270575   68.863    0.000 1258.838    0.000 categorical.py:88(logits)
             2076976160 1237.706    0.000 1237.706    0.000 {built-in method torch._C._get_tracing_state}
               55270575   70.503    0.000 1189.975    0.000 utils.py:82(probs_to_logits)
              165811725 1165.685    0.000 1165.685    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8934715405 1138.281    0.000 1156.082    0.000 {built-in method builtins.len}
              165811725 1044.113    0.000 1044.113    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8382519915 1011.338    0.000 1011.338    0.000 {method 'values' of 'collections.OrderedDict' objects}
              110541150  905.283    0.000  905.283    0.000 {built-in method broadcast_tensors}
               55270575  880.945    0.000  880.945    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2210823   83.924    0.000  755.252    0.000 replaybuffer.py:34(save_option_critic)
               55270575  146.801    0.000  691.032    0.000 utils.py:77(clamp_probs)
                2210823  106.964    0.000  680.584    0.000 optimizer.py:189(zero_grad)
              167469840  679.835    0.000  679.835    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               55270575  654.784    0.000  654.784    0.000 {built-in method bernoulli}
               55270575  579.025    0.000  579.025    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               55731247  551.873    0.000  551.873    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              332728860  550.812    0.000  550.812    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               55270575  544.231    0.000  544.231    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              165811750  147.449    0.000  539.456    0.000 {built-in method builtins.all}
              729915419  314.620    0.000  516.350    0.000 {built-in method builtins.isinstance}
              110541150  488.821    0.000  488.821    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               55270575   99.797    0.000  485.693    0.000 layers.py:838(isFree)
               55270575  474.186    0.000  474.186    0.000 {built-in method clamp}
               17686592  278.238    0.000  464.054    0.000 layer.py:175(NoRock_update)
               14923057  458.380    0.000  458.380    0.000 {built-in method tensor}
              166276841  448.324    0.000  448.324    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               30951516  438.928    0.000  438.928    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               55270575  428.440    0.000  428.440    0.000 {built-in method log}
               55270575  413.727    0.000  413.727    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              171891501  404.628    0.000  404.628    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              336949343  326.462    0.000  385.897    0.000 layer.py:103(isFree)
               30951516  376.952    0.000  376.952    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               55270575  369.138    0.000  369.138    0.000 {built-in method all}
               57481424  173.670    0.000  356.622    0.000 grad_mode.py:119(__enter__)
                6632473   13.978    0.000  356.498    0.000 game.py:38(board)
             1056993063  243.211    0.000  355.178    0.000 enum.py:646(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606122: <Attempt2_Diamonds3_option_critic_0> in cluster <dcc> Done

Job <Attempt2_Diamonds3_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:09 2021
Terminated at Thu May  6 01:28:28 2021
Results reported at Thu May  6 01:28:28 2021

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

    CPU time :                                   258288.00 sec.
    Max Memory :                                 905 MB
    Average Memory :                             891.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15479.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258920 sec.

The output (if any) is above this job summary.

