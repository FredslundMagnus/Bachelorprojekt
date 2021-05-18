
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH_2-0
    Main :                      Load_Cfagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal3_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      52816462231 function calls (52488442286 primitive calls) in 86111.69 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.688 86111.688 {built-in method builtins.exec}
                      1    4.327    4.327 86111.688 86111.688 <string>:1(<module>)
                      1  269.178  269.178 86107.361 86107.361 main.py:109(Load_Cfagent)
                2321360 3514.407    0.002 25173.117    0.011 agent.py:212(counterfact)
                6964080   28.351    0.000 23075.026    0.003 agent.py:29(learn)
                6964080  562.218    0.000 19298.343    0.003 learner.py:42(Qlearn)
        363089751/35072627 1662.006    0.000 14487.164    0.000 module.py:866(_call_impl)
               28108547   81.810    0.000 13800.416    0.000 network.py:28(forward)
               28108547  424.693    0.000 13515.608    0.000 container.py:117(forward)
                2321360   12.086    0.000 13406.026    0.006 game.py:42(step)
                2321360   14.873    0.000 12853.816    0.006 layers.py:827(step)
                5931922  132.276    0.000 10039.139    0.002 agent.py:176(choose_action)
                2321360  254.386    0.000 8885.757    0.004 agent.py:54(_learn)
               86894440 8266.544    0.000 8266.544    0.000 {built-in method tensor}
                2321360  254.231    0.000 8259.296    0.004 agent.py:204(_learn)
               10569825  297.487    0.000 8250.452    0.001 agent.py:49(__call__)
                6964080   64.022    0.000 8159.866    0.001 optimizer.py:84(wrapper)
               81774674   57.553    0.000 8148.386    0.000 game.py:38(board)
                6964080   31.712    0.000 7859.931    0.001 grad_mode.py:24(decorate_context)
                6964080  230.067    0.000 7757.601    0.001 adam.py:55(step)
                6964080 1594.951    0.000 7278.079    0.001 _functional.py:53(adam)
                2321360  208.637    0.000 7272.138    0.003 layers.py:17(step)
              232075580  394.389    0.000 7042.276    0.000 layer.py:106(move)
                2321360   74.701    0.000 5885.991    0.003 agent.py:117(_learn)
                2321360  367.697    0.000 5547.685    0.002 layers.py:793(update)
                2321360 2764.859    0.001 5150.092    0.002 replaybuffer.py:28(teleporter_save_data)
                6964080   25.540    0.000 4883.778    0.001 tensor.py:195(backward)
                6964080   27.812    0.000 4857.145    0.001 __init__.py:68(backward)
               56217094  131.242    0.000 4786.874    0.000 conv.py:398(forward)
                6964080 4662.013    0.001 4662.013    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               56217094   96.181    0.000 4591.279    0.000 conv.py:390(_conv_forward)
               56217094 4495.098    0.000 4495.098    0.000 {built-in method conv2d}
                2321360 2584.473    0.001 4393.854    0.002 agent.py:88(interveen)
               74283504 2392.278    0.000 4387.028    0.000 layer.py:175(NoRock_update)
                2321360 3393.500    0.001 4207.126    0.002 replaybuffer.py:22(sample_data)
                2321360 3400.339    0.001 4195.915    0.002 replaybuffer.py:67(sample_data)
              232075580  871.110    0.000 4164.348    0.000 layers.py:844(check)
               79682921  177.908    0.000 3923.060    0.000 linear.py:93(forward)
               79682921   70.832    0.000 3652.307    0.000 functional.py:1737(linear)
               79682921 3563.321    0.000 3563.321    0.000 {built-in method torch._C._nn.linear}
              167346675 2349.457    0.000 2349.457    0.000 {built-in method clone}
                2321360 1577.734    0.001 2307.401    0.001 agent.py:67(modify)
              107791468   93.440    0.000 2204.551    0.000 activation.py:713(forward)
              107791468   97.196    0.000 2111.111    0.000 functional.py:1364(leaky_relu)
              232075580  384.001    0.000 2103.029    0.000 layers.py:838(isFree)
                5931922 1798.466    0.000 2100.801    0.000 agent.py:187(convert_values)
              107791468 1993.591    0.000 1993.591    0.000 {built-in method torch._C._nn.leaky_relu}
               12891185   91.551    0.000 1993.041    0.000 agent.py:59(modify_board)
                2321360 1339.459    0.001 1833.883    0.001 replaybuffer.py:73(CF_save_data)
                5162438   55.810    0.000 1801.284    0.000 layers.py:849(restart)
             1732021644 1425.460    0.000 1719.028    0.000 layer.py:103(isFree)
               36104785 1581.981    0.000 1581.981    0.000 {built-in method cat}
              129996160 1497.956    0.000 1497.956    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              129996160 1313.841    0.000 1313.841    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5162438   26.662    0.000 1305.369    0.000 level.py:8(__init__)
                2321360   44.270    0.000 1282.151    0.001 agent.py:172(__call__)
               12891185 1267.044    0.000 1267.044    0.000 {built-in method torch._C._nn.one_hot}
                2321360   41.569    0.000 1180.802    0.001 agent.py:112(__call__)
                6964080  180.114    0.000 1125.912    0.000 optimizer.py:189(zero_grad)
              232136000  158.971    0.000 1094.974    0.000 {built-in method builtins.all}
             1149525661 1070.492    0.000 1070.492    0.000 layer.py:154(elements)
             3900006529  736.939    0.000 1058.054    0.000 enum.py:646(__hash__)
                5162438  111.542    0.000 1032.735    0.000 levels.py:164(generate)
             1703690743  487.508    0.000  965.910    0.000 layers.py:799(<genexpr>)
              233937641  218.456    0.000  900.928    0.000 {built-in method builtins.any}
              232075580  545.575    0.000  872.654    0.000 layers.py:246(check)
               10569825  309.581    0.000  845.912    0.000 exploration.py:53(softmaxer)
               64998080  810.982    0.000  810.982    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              232075580  476.837    0.000  804.347    0.000 layers.py:286(check)
               10324876  104.729    0.000  771.215    0.000 level.py:41(notUsed)
             9489470393  666.020    0.000  741.015    0.000 {built-in method builtins.len}
               64998080  696.962    0.000  696.962    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2042762058  558.664    0.000  682.472    0.000 layers.py:809(<genexpr>)
               64998080  677.823    0.000  677.823    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               64998080  664.681    0.000  664.681    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2321360   44.950    0.000  631.273    0.000 replaybuffer.py:18(stacker)
                2321360   47.266    0.000  619.345    0.000 replaybuffer.py:63(stacker)
              182559220  612.120    0.000  612.120    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2321360  319.017    0.000  528.697    0.000 collector.py:46(collect)
               64998080  513.653    0.000  513.653    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               14967596  170.572    0.000  454.038    0.000 random.py:315(sample)
               31088285  434.549    0.000  434.549    0.000 {method 'item' of 'torch._C._TensorBase' objects}
             4507135457  433.580    0.000  433.580    0.000 layer.py:99(positions)
              232075580  275.114    0.000  432.303    0.000 layers.py:313(check)
               41299504   52.636    0.000  424.667    0.000 layer.py:77(restart)
              454986560  339.005    0.000  417.641    0.000 tensor.py:906(grad)
              232075580  247.917    0.000  393.587    0.000 layers.py:273(check)
                6964080   11.464    0.000  365.454    0.000 loss.py:527(forward)
               56217094   46.720    0.000  364.079    0.000 flatten.py:39(forward)
                6964080   26.668    0.000  353.990    0.000 functional.py:2898(mse_loss)
               10324876   10.961    0.000  333.900    0.000 level.py:38(elementsIn)
              232075580  219.556    0.000  330.652    0.000 layers.py:48(check)
             3900033216  321.120    0.000  321.120    0.000 {built-in method builtins.hash}
               56217094  317.359    0.000  317.359    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              153160437  201.399    0.000  299.043    0.000 layers.py:113(isDone)
              502958671  204.077    0.000  287.863    0.000 layer.py:138(add)
              243382363  211.269    0.000  283.242    0.000 layer.py:134(remove)
              373666507  281.594    0.000  281.594    0.000 {built-in method torch._C._get_tracing_state}
               74283504  279.783    0.000  279.783    0.000 layer.py:186(<listcomp>)
               10569825  273.780    0.000  273.780    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632961: <Causal3_Conver4_3counterfactsNOCRASH_2_0> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:03 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 13 17:07:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 13 17:07:08 2021
Terminated at Fri May 14 17:02:27 2021
Results reported at Fri May 14 17:02:27 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85901.98 sec.
    Max Memory :                                 7767 MB
    Average Memory :                             5537.13 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8617.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            177684 sec.

The output (if any) is above this job summary.

