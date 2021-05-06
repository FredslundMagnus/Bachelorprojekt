
# Parameters

    Name :                      Attempt3_Maze_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Maze
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


      37241513978 function calls (36039338916 primitive calls) in 258894.35 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.724 258900.724 {built-in method builtins.exec}
                      1    0.340    0.340 258900.723 258900.723 <string>:1(<module>)
                      1 4319.463 4319.463 258900.384 258900.384 optionCritic.py:195(option_critic_run)
               43196150 8387.877    0.000 105088.617    0.002 optionCritic.py:143(actor_loss_fn)
        1595600999/393538544 10767.816    0.000 103401.361    0.000 module.py:866(_call_impl)
              133562495  814.867    0.000 95147.467    0.001 optionCritic.py:70(get_state)
              133562495 2457.927    0.000 91939.450    0.001 container.py:117(forward)
                1727846   12.358    0.000 58508.405    0.034 tensor.py:195(backward)
                1727846   18.430    0.000 58495.805    0.034 __init__.py:68(backward)
                1727846 58438.286    0.034 58438.286    0.034 {method 'run_backward' of 'torch._C._EngineBase' objects}
              267124990 1070.804    0.000 56173.486    0.000 conv.py:398(forward)
              267124990  637.237    0.000 54613.653    0.000 conv.py:390(_conv_forward)
              267124990 53976.417    0.000 53976.417    0.000 {built-in method conv2d}
                1727846   39.279    0.000 40093.032    0.023 optimizer.py:84(wrapper)
                1727846   26.608    0.000 39945.551    0.023 grad_mode.py:24(decorate_context)
                1727846  107.855    0.000 39878.404    0.023 rmsprop.py:56(step)
                1727846  140.813    0.000 39647.887    0.023 _functional.py:203(rmsprop)
               24189826 35946.952    0.001 35946.952    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               43196150 3586.598    0.000 20929.552    0.000 optionCritic.py:91(get_action)
              527101039 1775.368    0.000 19596.716    0.000 linear.py:93(forward)
              527101039  660.096    0.000 17007.255    0.000 functional.py:1737(linear)
              527101039 16215.866    0.000 16215.866    0.000 {built-in method torch._C._nn.linear}
               43196150 1198.071    0.000 13336.277    0.000 optionCritic.py:80(predict_option_termination)
               86392300 1177.737    0.000 7717.532    0.000 distribution.py:34(__init__)
              400687485  587.692    0.000 7471.511    0.000 activation.py:713(forward)
               43196150  595.165    0.000 6980.470    0.000 categorical.py:115(log_prob)
              400687485  489.553    0.000 6883.819    0.000 functional.py:1364(leaky_relu)
              400687485 6286.812    0.000 6286.812    0.000 {built-in method torch._C._nn.leaky_relu}
              130214815  488.813    0.000 6052.462    0.000 optionCritic.py:77(get_Q)
               43196150  805.793    0.000 5903.802    0.000 categorical.py:49(__init__)
               43196150  346.741    0.000 4820.540    0.000 bernoulli.py:34(__init__)
               86565084  441.975    0.000 4543.554    0.000 optionCritic.py:88(get_terminations)
               43196150 2404.272    0.000 3552.515    0.000 constraints.py:398(check)
                1727846   10.065    0.000 3219.592    0.002 game.py:42(step)
                1727846   19.288    0.000 3100.802    0.002 layers.py:827(step)
               43196150  477.208    0.000 2751.095    0.000 distribution.py:240(_validate_sample)
               24189826 2515.601    0.000 2515.601    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2068387447 2262.196    0.000 2262.199    0.000 module.py:934(__getattr__)
                 172784   31.801    0.000 2033.357    0.012 optionCritic.py:116(critic_loss_fn)
              133562495  202.038    0.000 1981.909    0.000 activation.py:101(forward)
               43196150 1949.338    0.000 1949.338    0.000 constraints.py:364(check)
               43196150  951.797    0.000 1929.863    0.000 categorical.py:123(entropy)
               43196150  367.166    0.000 1789.423    0.000 bernoulli.py:86(sample)
              133562495  157.110    0.000 1779.871    0.000 functional.py:1195(relu)
              129588450  231.336    0.000 1776.020    0.000 utils.py:106(__get__)
                1727846   70.630    0.000 1757.554    0.001 layers.py:17(step)
               43196150 1753.179    0.000 1753.179    0.000 constraints.py:249(check)
               43196150  127.644    0.000 1680.619    0.000 layer.py:106(move)
              133562495 1595.467    0.000 1595.467    0.000 {built-in method relu}
              302373050 1526.122    0.000 1526.122    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              133562495  162.521    0.000 1488.325    0.000 flatten.py:39(forward)
              129934018  180.707    0.000 1465.510    0.000 tensor.py:525(__rsub__)
             1614607305 1446.843    0.000 1446.843    0.000 {built-in method torch._C._get_tracing_state}
               86392300  518.929    0.000 1410.194    0.000 functional.py:46(broadcast_tensors)
               43196150   73.689    0.000 1366.280    0.000 categorical.py:88(logits)
               43196150  353.403    0.000 1337.732    0.000 categorical.py:108(sample)
              133562495 1325.804    0.000 1325.804    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1727847  160.381    0.000 1316.160    0.001 layers.py:793(update)
               43196150   76.971    0.000 1292.591    0.000 utils.py:82(probs_to_logits)
              129588450 1264.659    0.000 1264.659    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              129934018 1258.863    0.000 1258.863    0.000 {built-in method rsub}
              129761234 1157.923    0.000 1157.923    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               19006306   47.637    0.000 1083.946    0.000 tensor.py:575(__iter__)
               86565084 1081.120    0.000 1081.120    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             6932992630 1038.052    0.000 1051.943    0.000 {built-in method builtins.len}
               43196150  205.433    0.000 1043.458    0.000 utils.py:11(broadcast_all)
               19006306 1005.675    0.000 1005.675    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               43196150  241.487    0.000  976.948    0.000 layers.py:844(check)
              129588450  932.549    0.000  932.549    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6515966491  895.592    0.000  895.592    0.000 {method 'values' of 'collections.OrderedDict' objects}
               43196150  155.638    0.000  807.908    0.000 utils.py:77(clamp_probs)
               43196150  805.801    0.000  805.801    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               86392300  754.045    0.000  754.045    0.000 {built-in method broadcast_tensors}
               43196150  652.270    0.000  652.270    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               43196150  649.451    0.000  649.451    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1727846   71.948    0.000  633.596    0.000 replaybuffer.py:34(save_option_critic)
              130106802  609.609    0.000  609.609    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               43476947  557.518    0.000  557.518    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               43196150  542.015    0.000  542.015    0.000 {built-in method bernoulli}
               43196150  533.687    0.000  533.687    0.000 {built-in method clamp}
               86392300  530.930    0.000  530.930    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1727846   89.413    0.000  502.894    0.000 optimizer.py:189(zero_grad)
              259522468  496.239    0.000  496.239    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               43196150  106.273    0.000  493.647    0.000 layers.py:838(isFree)
               13822776  252.547    0.000  422.743    0.000 layer.py:175(NoRock_update)
               43196150  414.722    0.000  414.722    0.000 {built-in method all}
               24189826  413.881    0.000  413.881    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               43196150  407.712    0.000  407.712    0.000 {built-in method log}
              297788996  318.284    0.000  387.374    0.000 layer.py:103(isFree)
               43196150  379.488    0.000  379.488    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                 172784  282.453    0.002  353.947    0.002 replaybuffer.py:42(sample_option_critic)
              570924296  235.548    0.000  351.376    0.000 {built-in method builtins.isinstance}
                 280821    6.816    0.000  340.079    0.001 layers.py:849(restart)
               24189826  332.513    0.000  332.513    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10885432  326.227    0.000  326.227    0.000 {built-in method tensor}
              129872725  325.379    0.000  325.379    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               43196150  321.165    0.000  321.165    0.000 {built-in method multinomial}
              133562509  305.289    0.000  305.289    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               24189826  298.127    0.000  298.127    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 280821    4.181    0.000  293.418    0.001 level.py:8(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607861: <Attempt3_Maze_option_critic_0> in cluster <dcc> Done

Job <Attempt3_Maze_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
Job was executed on host(s) <n-62-21-101>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:27 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

    CPU time :                                   258114.89 sec.
    Max Memory :                                 900 MB
    Average Memory :                             884.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15484.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259010 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

