
# Parameters

    Name :                      Causal4_Cf_convert3_TopN6-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68350626914 function calls (68048356199 primitive calls) in 86117.43 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.431 86117.431 {built-in method builtins.exec}
                      1    4.780    4.780 86117.431 86117.431 <string>:1(<module>)
                      1  420.584  420.584 86112.651 86112.651 main.py:79(CFagent)
                9912390   41.894    0.000 25521.803    0.003 agent.py:29(learn)
                3304130   17.351    0.000 21296.531    0.006 game.py:41(step)
                9912387  651.947    0.000 20565.015    0.002 learner.py:42(Qlearn)
                3304130   22.957    0.000 20468.002    0.006 layers.py:718(step)
                3304130  326.101    0.000 13790.239    0.004 layers.py:17(step)
              330073257 1026.198    0.000 13431.357    0.000 layer.py:98(move)
        338471873/36202849 1493.774    0.000 11696.147    0.000 module.py:866(_call_impl)
               26290462   75.345    0.000 10903.435    0.000 network.py:27(forward)
               26290462  363.007    0.000 10643.376    0.000 container.py:117(forward)
                3304130  832.934    0.000 10100.918    0.003 agent.py:210(counterfact)
                3304130  411.095    0.000 9958.677    0.003 agent.py:54(_learn)
                3304130  401.609    0.000 9051.815    0.003 agent.py:202(_learn)
              330073257 1554.165    0.000 8270.035    0.000 layers.py:735(check)
                9912387   96.412    0.000 7898.452    0.001 optimizer.py:84(wrapper)
                3304130 6713.565    0.002 7842.141    0.002 replaybuffer.py:22(sample_data)
                3304130 6490.081    0.002 7565.131    0.002 replaybuffer.py:67(sample_data)
                9912387   50.468    0.000 7481.598    0.001 grad_mode.py:24(decorate_context)
                9912387  335.219    0.000 7326.007    0.001 adam.py:55(step)
                9912387 1511.809    0.000 6635.031    0.001 _functional.py:53(adam)
                3304131  517.197    0.000 6620.512    0.002 layers.py:684(update)
                3304130  112.734    0.000 6445.590    0.002 agent.py:117(_learn)
                8180991  246.084    0.000 5667.110    0.001 agent.py:49(__call__)
               51746947 5574.633    0.000 5574.633    0.000 {built-in method tensor}
                9912387   44.579    0.000 5399.786    0.001 tensor.py:195(backward)
               44138824   28.444    0.000 5373.533    0.000 game.py:37(board)
                9912387   46.409    0.000 5353.735    0.001 __init__.py:68(backward)
                9912387 5087.898    0.001 5087.898    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               66082610 2774.144    0.000 4771.472    0.000 layer.py:151(update)
               52580924  123.943    0.000 3952.787    0.000 conv.py:398(forward)
                3304130 1645.301    0.000 3892.470    0.001 agent.py:88(interveen)
               52580924   97.268    0.000 3764.838    0.000 conv.py:390(_conv_forward)
               52580924 3667.571    0.000 3667.571    0.000 {built-in method conv2d}
              330073257  576.211    0.000 3447.847    0.000 layers.py:729(isFree)
                3304130 1836.171    0.001 3162.841    0.001 replaybuffer.py:28(teleporter_save_data)
               72263126  151.104    0.000 2960.680    0.000 linear.py:93(forward)
             2739432037 2430.992    0.000 2871.636    0.000 layer.py:95(isFree)
               72263126   61.853    0.000 2728.437    0.000 functional.py:1737(linear)
               72263126 2651.422    0.000 2651.422    0.000 {built-in method torch._C._nn.linear}
                3304130 1682.555    0.001 2576.059    0.001 agent.py:67(modify)
                1588827   37.094    0.000 2204.138    0.001 agent.py:175(choose_action)
               44526406 1799.775    0.000 1799.775    0.000 {built-in method cat}
             6121279908 1156.176    0.000 1635.583    0.000 enum.py:646(__hash__)
               11485121   83.419    0.000 1615.680    0.000 agent.py:59(modify_board)
                3304127   66.896    0.000 1588.645    0.000 agent.py:171(__call__)
               98553588   86.634    0.000 1570.297    0.000 activation.py:713(forward)
              330816794  354.331    0.000 1500.542    0.000 {built-in method builtins.any}
               98553588   87.622    0.000 1483.663    0.000 functional.py:1364(leaky_relu)
                3304130   62.753    0.000 1479.028    0.000 agent.py:112(__call__)
              330073257 1050.922    0.000 1381.981    0.000 layers.py:77(check)
               98553588 1377.733    0.000 1377.733    0.000 {built-in method torch._C._nn.leaky_relu}
              126420490 1323.478    0.000 1323.478    0.000 {built-in method clone}
              185031220 1299.134    0.000 1299.134    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              330073257  801.364    0.000 1200.162    0.000 layers.py:246(check)
             1049764904 1180.679    0.000 1180.679    0.000 layer.py:146(elements)
                9912387  208.311    0.000 1155.500    0.000 optimizer.py:189(zero_grad)
             3602639293  950.136    0.000 1146.212    0.000 layers.py:700(<genexpr>)
              185031220 1143.827    0.000 1143.827    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3304130  914.012    0.000 1141.460    0.000 replaybuffer.py:73(CF_save_data)
                2900437   40.368    0.000 1128.573    0.000 layers.py:740(restart)
               11485121 1067.533    0.000 1067.533    0.000 {built-in method torch._C._nn.one_hot}
              330073257  659.678    0.000 1066.911    0.000 layers.py:286(check)
                3304130   73.550    0.000  858.013    0.000 replaybuffer.py:18(stacker)
              330413100  158.374    0.000  833.709    0.000 {built-in method builtins.all}
                3304127   75.399    0.000  816.387    0.000 replaybuffer.py:63(stacker)
              330073257  643.136    0.000  799.521    0.000 layers.py:62(check)
                2900437   19.030    0.000  797.127    0.000 level.py:8(__init__)
               92515610  757.222    0.000  757.222    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7899019864  723.622    0.000  723.622    0.000 layer.py:91(positions)
             1704503666  445.880    0.000  715.971    0.000 layers.py:690(<genexpr>)
               92515610  659.505    0.000  659.505    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8747166325/8747166322  575.371    0.000  639.585    0.000 {built-in method builtins.len}
                2900437  105.377    0.000  631.037    0.000 levels.py:199(generate)
               92515610  623.295    0.000  623.295    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92515610  614.634    0.000  614.634    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8180991  209.364    0.000  585.245    0.000 exploration.py:53(softmaxer)
               12409134  218.935    0.000  566.136    0.000 random.py:315(sample)
              330073257  363.827    0.000  560.796    0.000 layers.py:273(check)
              647609354  444.754    0.000  549.192    0.000 tensor.py:906(grad)
              330073257  345.859    0.000  533.656    0.000 layers.py:313(check)
                3304130  301.291    0.000  514.249    0.000 collector.py:46(collect)
             6121317571  479.413    0.000  479.413    0.000 {built-in method builtins.hash}
              330073257  329.613    0.000  477.823    0.000 layers.py:48(check)
                9912387   18.596    0.000  474.862    0.000 loss.py:527(forward)
                9912387   47.333    0.000  456.265    0.000 functional.py:2898(mse_loss)
               92515610  452.594    0.000  452.594    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5800874   51.604    0.000  425.840    0.000 level.py:41(notUsed)
                1588827  345.669    0.000  366.116    0.000 agent.py:186(convert_values)
              330073257  244.540    0.000  362.862    0.000 layers.py:23(check)
             3643151011  300.129    0.000  300.129    0.000 {method 'random' of '_random.Random' objects}
              141209738  299.625    0.000  299.625    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              284200919  206.900    0.000  291.753    0.000 layer.py:126(remove)
               29004370   41.468    0.000  281.034    0.000 layer.py:69(restart)
                6608262  279.855    0.000  279.855    0.000 {built-in method nonzero}
               66082610  279.402    0.000  279.402    0.000 layer.py:163(<listcomp>)
              459417088  202.224    0.000  277.402    0.000 layer.py:130(add)
                9912387  274.789    0.000  274.789    0.000 {built-in method torch._C._nn.mse_loss}
              389984121  177.928    0.000  262.844    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533962: <Causal4_Cf_convert3_TopN6_1> in cluster <dcc> Done

Job <Causal4_Cf_convert3_TopN6_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 19 20:15:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 20:15:45 2021
Terminated at Tue Apr 20 20:11:11 2021
Results reported at Tue Apr 20 20:11:11 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85906.39 sec.
    Max Memory :                                 9455 MB
    Average Memory :                             6235.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6929.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            172264 sec.

The output (if any) is above this job summary.

