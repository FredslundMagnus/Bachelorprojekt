
# Parameters

    Name :                      Attempt6_Maze_option_critic-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      32785258844 function calls (31743445338 primitive calls) in 258886.49 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.765 258900.765 {built-in method builtins.exec}
                      1    0.318    0.318 258900.764 258900.764 <string>:1(<module>)
                      1 3796.459 3796.459 258900.446 258900.446 optionCritic.py:195(option_critic_run)
                1167952    8.763    0.000 136434.374    0.117 tensor.py:195(backward)
                1167952   11.830    0.000 136425.448    0.117 __init__.py:68(backward)
                1167952 136389.560    0.117 136389.560    0.117 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1379254359/341237010 6621.486    0.000 75536.875    0.000 module.py:866(_call_impl)
               37374464 5601.088    0.000 74616.381    0.002 optionCritic.py:143(actor_loss_fn)
              115335261  568.971    0.000 70492.037    0.001 optionCritic.py:70(get_state)
              115335261 1529.573    0.000 68260.030    0.001 container.py:117(forward)
              230670522  632.119    0.000 40901.684    0.000 conv.py:398(forward)
              230670522  348.108    0.000 40011.079    0.000 conv.py:390(_conv_forward)
              230670522 39662.971    0.000 39662.971    0.000 {built-in method conv2d}
              456572271 1100.759    0.000 17069.076    0.000 linear.py:93(forward)
              456572271  443.076    0.000 15512.535    0.000 functional.py:1737(linear)
              456572271 14968.792    0.000 14968.792    0.000 {built-in method torch._C._nn.linear}
               37374464 2158.155    0.000 12975.715    0.000 optionCritic.py:91(get_action)
               37374464  809.139    0.000 9545.205    0.000 optionCritic.py:80(predict_option_termination)
                1167952   24.676    0.000 6855.512    0.006 optimizer.py:84(wrapper)
                1167952   15.106    0.000 6760.928    0.006 grad_mode.py:24(decorate_context)
                1167952   71.052    0.000 6720.814    0.006 adam.py:55(step)
                1167952  414.725    0.000 6573.516    0.006 _functional.py:53(adam)
               74748928  816.410    0.000 5204.480    0.000 distribution.py:34(__init__)
              346005783  354.236    0.000 4693.092    0.000 activation.py:713(forward)
               37374464  369.980    0.000 4360.796    0.000 categorical.py:115(log_prob)
              346005783  370.300    0.000 4338.857    0.000 functional.py:1364(leaky_relu)
              346005783 3893.026    0.000 3893.026    0.000 {built-in method torch._C._nn.leaky_relu}
              113486369  267.115    0.000 3777.145    0.000 optionCritic.py:77(get_Q)
               37374464  293.430    0.000 3766.532    0.000 bernoulli.py:34(__init__)
               37374464  481.230    0.000 3628.171    0.000 categorical.py:49(__init__)
                 291988   48.544    0.000 3214.781    0.011 optionCritic.py:116(critic_loss_fn)
               75040916  268.822    0.000 2908.144    0.000 optionCritic.py:88(get_terminations)
                1167952    6.899    0.000 2689.767    0.002 game.py:42(step)
                1167952   10.312    0.000 2606.739    0.002 layers.py:827(step)
               37374464 1473.301    0.000 2201.709    0.000 constraints.py:398(check)
               37374464  307.904    0.000 1765.366    0.000 distribution.py:240(_validate_sample)
               32702644 1468.645    0.000 1468.645    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1167953  104.775    0.000 1454.480    0.001 layers.py:793(update)
               37374464  289.817    0.000 1433.365    0.000 bernoulli.py:86(sample)
               37374464 1413.798    0.000 1413.798    0.000 constraints.py:364(check)
              115335261  155.792    0.000 1369.858    0.000 activation.py:101(forward)
               16351322 1263.271    0.000 1263.271    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1790623411 1223.127    0.000 1223.212    0.000 module.py:934(__getattr__)
              115335261  131.486    0.000 1214.066    0.000 functional.py:1195(relu)
               37374464  620.685    0.000 1190.906    0.000 categorical.py:123(entropy)
              261621248 1172.500    0.000 1172.500    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               37374464 1146.073    0.000 1146.073    0.000 constraints.py:249(check)
                1167952   50.033    0.000 1136.825    0.001 layers.py:17(step)
               16351322 1106.793    0.000 1106.793    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37374464   81.121    0.000 1081.902    0.000 layer.py:106(move)
              112123392  142.744    0.000 1080.821    0.000 utils.py:106(__get__)
              115335261  119.472    0.000 1068.343    0.000 flatten.py:39(forward)
              115335261 1062.270    0.000 1062.270    0.000 {built-in method relu}
              112707368  127.180    0.000 1041.251    0.000 tensor.py:525(__rsub__)
               74748928  363.714    0.000 1028.828    0.000 functional.py:46(broadcast_tensors)
              115335261  948.871    0.000  948.871    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              112707368  894.507    0.000  894.507    0.000 {built-in method rsub}
               37374464  177.245    0.000  870.604    0.000 utils.py:11(broadcast_all)
               37374464  235.588    0.000  851.217    0.000 categorical.py:108(sample)
               75040916  846.678    0.000  846.678    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               37374464   42.287    0.000  822.858    0.000 categorical.py:88(logits)
              112415380  813.223    0.000  813.223    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               12847472   30.057    0.000  809.181    0.000 tensor.py:575(__iter__)
             1392101831  800.831    0.000  800.831    0.000 {built-in method torch._C._get_tracing_state}
               16351322  782.759    0.000  782.759    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               37374464   47.170    0.000  780.571    0.000 utils.py:82(probs_to_logits)
               32702644  770.888    0.000  770.888    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             6012117747  760.883    0.000  769.152    0.000 {built-in method builtins.len}
                 779032   14.787    0.000  764.363    0.001 layers.py:849(restart)
               37374464  177.925    0.000  761.708    0.000 layers.py:844(check)
               12847472  760.791    0.000  760.791    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               16351322  759.947    0.000  759.947    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              112123392  756.665    0.000  756.665    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 779032    9.327    0.000  658.970    0.001 level.py:8(__init__)
              112123392  651.915    0.000  651.915    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5632352697  646.970    0.000  646.970    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1063312   83.376    0.000  592.858    0.001 levels.py:9(generate)
               37374464  570.660    0.000  570.660    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 291988  460.991    0.002  569.894    0.002 replaybuffer.py:42(sample_option_critic)
               74748928  542.985    0.000  542.985    0.000 {built-in method broadcast_tensors}
                1167952   53.521    0.000  461.053    0.000 replaybuffer.py:34(save_option_critic)
               37374464   94.492    0.000  460.716    0.000 utils.py:77(clamp_probs)
               37374464  439.861    0.000  439.861    0.000 {built-in method bernoulli}
              112999356  422.146    0.000  422.146    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               38153465  374.724    0.000  374.724    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37374464  366.224    0.000  366.224    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               37374464  366.191    0.000  366.191    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              224830760  347.969    0.000  347.969    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               74748928  317.620    0.000  317.620    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                9343624  190.875    0.000  316.596    0.000 layer.py:175(NoRock_update)
                1167952   54.784    0.000  313.934    0.000 optimizer.py:189(zero_grad)
               37374464  302.523    0.000  302.523    0.000 {built-in method clamp}
              497701205  189.773    0.000  291.770    0.000 {built-in method builtins.isinstance}
               37374464  272.685    0.000  272.685    0.000 {built-in method log}
               37374464  263.189    0.000  263.189    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              115335275  262.988    0.000  262.988    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              112904758  253.024    0.000  253.024    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               37374464  138.224    0.000  251.320    0.000 layers.py:168(check)
               37374464  245.693    0.000  245.693    0.000 {built-in method all}
                7883680  235.163    0.000  235.163    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624167: <Attempt6_Maze_option_critic_2> in cluster <dcc> Done

Job <Attempt6_Maze_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
Job was executed on host(s) <n-62-11-61>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:29 2021
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

    CPU time :                                   258290.17 sec.
    Max Memory :                                 947 MB
    Average Memory :                             937.35 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15437.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258907 sec.

The output (if any) is above this job summary.

